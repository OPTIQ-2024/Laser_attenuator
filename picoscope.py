import numpy as np
from PyQt5 import QtCore
from picosdk import ps2000a


class PicoscopeScope(QtCore.QObject):

    current_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.scope = None      # Objet représentant l'oscilloscope PS2000a 
        self.handle = None     # Handle de l'oscilloscope
        self.sample_rate = 1e6 # Taux d'échantillonnage
        self.timebase = 50e-6  # Temps de base de l'échantillonnage
        self.samples = 1024    # Nombre d'échantillons à capturer 
        self.channel_range = 2.0  # Plage de tension (±2 V par défaut)

    def connect(self): 
        """Initialisation de la connexion au Picoscope PS2000a"""
        self.scope = ps2000a.PS2000a()
        status = self.scope.open()
        if status != 0:
            print("Erreur de connexion à l'oscilloscope")
        else:
            print("Connexion à l'oscilloscope réussie")
            print(self.scope.getAllUnitInfo())

    def configure_scope(self):
        """Configuration des paramètres de l'oscilloscope"""
        if self.scope is None:
            print("Oscilloscope non connecté")
            return

        # Configuration du canal
        self.channel_range = self.scope.setChannel(
            channel='A', 
            coupling='DC', 
            range=self.channel_range, 
            offset=0.0, 
            enabled=True, 
            BWLimited=False
        )
        print(f"Plage de canal choisie : ±{self.channel_range} V")

        # Configuration du déclencheur
        self.scope.setSimpleTrigger('A', threshold=1.0, direction='Falling', timeout_ms=100, enabled=True)

    def capture_data(self):
        """Capture des données récupérées par l'oscilloscope"""
        if self.scope is None:
            print("Oscilloscope non connecté")
            return

        # Configuration du temps d'échantillonnage
        obs_duration = 3 * self.timebase
        sampling_interval = obs_duration / self.samples
        actual_sampling_interval, n_samples, max_samples = self.scope.setSamplingInterval(
            sampling_interval, obs_duration
        )
        print(f"Taux d'échantillonnage réel : {actual_sampling_interval * 1e9:.2f} ns")
        print(f"Nombre d'échantillons : {n_samples}, Maximum : {max_samples}")

        # Acquisition des données
        self.scope.runBlock()
        self.scope.waitReady()
        print("Acquisition terminée")

        data = self.scope.getDataV('A', n_samples, returnOverflow=False)
        time_axis = np.arange(n_samples) * actual_sampling_interval

        self.current_plot.emit(time_axis, data)

    def close_scope(self):
        """Interruption de la connexion avec l'oscilloscope"""
        if self.scope is not None:
            self.scope.stop()
            self.scope.close()
            self.scope = None
            print("Connexion avec l'oscilloscope interrompue")

    




