import numpy as np
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import TextItem

from ui_scope import Ui_ScopeViewer
import capture_ps2000a 


class ScopeThread(QtCore.QThread):

    new_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, scope, parent=None):
        super().__init__()
        self.scope = scope
        self.scope.current_plot.connect(self.send_new_plot)

    def __del__(self):
        self.wait()

    def stop_thread(self):
        self.running = False

    def start_thread(self):
        self.running = True

    def send_new_plot(self, t, amplitude):
        self.new_plot.emit(t, amplitude)


    def run(self):
        while (self.running):
            self.scope.get_plot()
            time.sleep(0.5)



class ScopeViewer(QMainWindow):
    def __init__(self, parent=None):

        super().__init__()
        self.ui = Ui_ScopeViewer()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushbutton_connect.clicked.connect(self.connect)
        self.ui.pushbutton_start.clicked.connect(self.start)
        self.ui.pushbutton_stop.clicked.connect(self.stop)

        self.plot = self.ui.plot_widget 
        self.plot.setLabel('left', 'Voltage (V)')  # Configure l'axe vertical
        self.plot.setLabel('bottom', 'Time (s)')  # Configure l'axe horizontal
        self.plot.setYRange(-0.01,0.2)
        self.avg_text = TextItem("", color="b")  # Valeur moyenne
        self.avg_text.setPos(0, 0.15)  # Position initiale
        self.plot.addItem(self.avg_text)
        self.plot.showGrid(x=True, y=True)  


    def connect(self):
        self.scope = capture_ps2000a.BlockMode()
        self.scope.set_channels('A')
        self.scope.set_sampling()
        self.scope.set_sig_gen()
        self.scope_thread = ScopeThread(self.scope)
        self.scope_thread.new_plot.connect(self.display_new_plot)
        print("Scope connected")

    def start(self):
        self.scope_thread.start_thread()
        self.scope_thread.start()

    def stop(self):
        self.scope_thread.stop_thread()

    def display_new_plot(self, time, amplitude):
        self.time = time
        self.amplitude = amplitude[0]
        self.plot.clear()
        self.plot.plot(self.time, self.amplitude, pen='b')
         # Calcul de la tension moyenne
        avg_voltage = np.mean(self.amplitude)
        self.avg_text.setText(f"Tension moyenne : {avg_voltage:.3f} V")
        self.plot.addItem(self.avg_text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ScopeViewer()
    window.show()
    sys.exit(app.exec_())