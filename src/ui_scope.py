from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget

from pyqtgraph import PlotWidget

class Ui_ScopeViewer():
    def setupUi(self, parent):

        parent.setWindowTitle("Scope Viewer")

        widget = QWidget()
        parent.setCentralWidget(widget)

        # Creation du layout verticale
        self.layout_v = QVBoxLayout()
        widget.setLayout(self.layout_v)

        # Création du conteneur pour les boutons (alignement horizontal)
        widget_h1 = QWidget()
        self.layout_h1 = QHBoxLayout()  
        widget_h1.setLayout(self.layout_h1)
        self.layout_v.addWidget(widget_h1)


        # Creation des 3 boutons
        self.pushbutton_connect = QPushButton("Connect")
        self.pushbutton_start = QPushButton("Start")
        self.pushbutton_stop = QPushButton("Stop")

        # Insertion des boutons dans le layout horizontal
        self.layout_h1.addWidget(self.pushbutton_connect)
        self.layout_h1.addWidget(self.pushbutton_start)
        self.layout_h1.addWidget(self.pushbutton_stop)
        
        # Creation d'un conteneur pour le graphe 
        widget_h3 = QWidget()
        self.layout_v.addWidget(widget_h3)

        # Creation d'un layout pour le graphe
        self.plot_layout = QVBoxLayout()
        self.plot_widget = PlotWidget(title="Tension en fonction du temps")
        self.plot_widget.setBackground('w')  # Changer le fond en blanc
        self.plot_layout.addWidget(self.plot_widget)
        widget_h3.setLayout(self.plot_layout)
