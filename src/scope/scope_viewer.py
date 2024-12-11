"""Ce programme sert à contrôler un oscilloscope de type Picoscope2406B et d'afficher en temps réel les signaux mesurés par l'oscilloscope via une interface graphique"""

import numpy as np
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import TextItem

from ui_scope import Ui_ScopeViewer
import capture_ps2000a 


class ScopeThread(QtCore.QThread):

    """Cette classe sert à exécuter des taches en arrière plan sans bloquer l'interface"""

    new_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, scope, parent=None):

        """Initialisation du thread et connection au signal"""

        super().__init__()
        self.scope = scope
        self.scope.current_plot.connect(self.send_new_plot)

    def __del__(self):

        """Attend la fin du thread avant de le détruire"""

        self.wait()

    def stop_thread(self):

        """Met à jour self.running pour arreter la boucle dans run"""

        self.running = False

    def start_thread(self):

        """Active self.running pour indiquer que le thread doit fonctionner"""

        self.running = True

    def send_new_plot(self, t, amplitude):

        """Emet un signal contenant les données en temps et en amplitude récupérées"""

        self.new_plot.emit(t, amplitude)


    def run(self):

        """Boucle principale du thread: récupère les données de l'oscilloscope et les envoies toutes les 0.5s tant que self.running est vrai"""

        while (self.running):
            self.scope.get_plot()
            time.sleep(0.5)



class ScopeViewer(QMainWindow):

    """Classe représentant la fenêtre principale de notre interface graphique. 
    Elle gère l'interaction entre l'utilisateur et l'oscilloscope"""

    def __init__(self, parent=None):

        """Initialisation de l'interface avec la configuration des boutons et des axes du graphes ainsi que l'affichage de le tension moyenne"""

        super().__init__()
        self.ui = Ui_ScopeViewer()
        self.ui.setupUi(self)

        # Connection des boutons
        self.ui.pushbutton_connect.clicked.connect(self.connect)
        self.ui.pushbutton_start.clicked.connect(self.start)
        self.ui.pushbutton_stop.clicked.connect(self.stop)

        #Configuration du graphe
        self.plot = self.ui.plot_widget 
        self.plot.setLabel('left', 'Voltage (V)')  # Configure l'axe vertical
        self.plot.setLabel('bottom', 'Time (s)')  # Configure l'axe horizontal
        self.plot.setYRange(-0.01,2)
        self.avg_text = TextItem("", color="b")  # Valeur moyenne
        self.avg_text.setPos(0, 0.15)  # Position initiale
        self.plot.addItem(self.avg_text)
        self.plot.showGrid(x=True, y=True)  


    def connect(self):

        """Configuration de l'oscilloscope"""

        self.scope = capture_ps2000a.BlockMode()
        self.scope.set_channels('A')
        self.scope.set_sampling()
        self.scope.set_sig_gen()

        # Creation d'une instance 
        self.scope_thread = ScopeThread(self.scope)

        # Connection du signal à la méthode display_new_plot
        self.scope_thread.new_plot.connect(self.display_new_plot)

        print("Scope connected")

    def start(self):

        """Activation du thread"""

        self.scope_thread.start_thread()
        self.scope_thread.start()

    def stop(self):

        """Interruption du thread"""

        self.scope_thread.stop_thread()

    def display_new_plot(self, time, amplitude):

        """Affichage des données reçues sur le graphe"""
        
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