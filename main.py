import sys
import time
from PyQt5 import QtGui, QtWidgets, QtCore

from ui_motor import Ui_MainWindow

from pypot.dynamixel.io import DxlIO


# Main application class

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Pushbuttons connections
        self.ui.pushbutton_connect.clicked.connect(self.connect)
        self.ui.pushbutton_close.clicked.connect(self.close)
        self.ui.dblspinbox_set_pos.valueChanged.connect(self.set_position)

    # Slots definition
    def connect(self):
        self.dxlio = DxlIO("/dev/tty.usbserial-FT2H2Y2W", baudrate=1000000)
        self.m_id = self.dxlio.scan(ids=range(5))

    def close(self):
        self.dxlio.close()

    def set_position(self, value):
        self.dxlio.set_goal_position({self.m_id[0]: value})
        time.sleep(0.1)
        current_pos = self.dxlio.get_present_position(self.m_id)
        self.ui.label_current_pos.setText(f'Current Position: {current_pos[0]}')


    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())