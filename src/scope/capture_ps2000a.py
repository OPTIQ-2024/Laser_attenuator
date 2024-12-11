'''
Ce programme est conçu pour capturer des données avec le PicoScope série 2000, en fonction du mode considéré.

'''

import time
import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import QtCore

from ps2000a import PS2000a

class BlockMode(QtCore.QObject):

    """Permet d'intéragir avec l'oscilloscope en mode 'Block Mode' 
    Elle permet de configurer les paramètres, acquérir les données et de transmettre aux autres parties du programme via des signaux PyQt. """

    current_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, parent=None):

        """Creation d'une instance de l'oscillscope via la classe PS2000a"""

        super().__init__(parent)  
        self.ps = PS2000a()

    def set_sampling(self, obs_duration=150e-6, num_samples = 4096):

        """Configuration de l'oscilloscope"""

        self.obs_duration = obs_duration # Durée totale de l'acquisition (s)
        self.num_samples = num_samples   # Nombre totale d'échnatillon à collecter
        self.sampling_interval = self.obs_duration / self.num_samples # Calcul de l'intervalle d'échantillonnage
        self.actual_sampling_interval, self.actual_num_samples, self.max_samples = self.ps.setSamplingInterval(
            self.sampling_interval, self.obs_duration)    
        self.time = np.arange(self.actual_num_samples) * self.actual_sampling_interval # Creation d'un axe tempore

    def set_channels(self,
                     channel='A',
                     coupling='DC',
                     vrange=2.0,
                     offset=0.0,
                     enabled=True,
                     BWLimited=False):
        
        """Configuration d'un canal spécifique de l'oscilloscope"""

        self.ps.setChannel(channel, coupling, vrange, offset, enabled,
                           BWLimited)

    def set_triggers(self,
                     trig_src='A',
                     threshold=0.5,
                     direction='Falling',
                     delay=0,
                     timeout_ms=100,
                     enabled=True):
        
        """Configuration d'un trigger simple sur l'oscilloscope"""

        self.ps.setSimpleTrigger(trig_src, threshold, direction, delay,
                                 timeout_ms, enabled)

    def set_sig_gen(self,
                    offsetVoltage=0,
                    pkToPk=2.0,
                    waveType="Sine",
                    frequency=50E3):
        
        """Configuration du générateur de signal intégré de l'oscilloscope"""

        self.ps.setSigGenBuiltInSimple(offsetVoltage, pkToPk, waveType,
                                       frequency)

    def get_data(self, channel='A', actual_num_samples=0):

        """Récuperation des données acquises par l'oscilloscope pour un canal spécifique et les stocke"""

        self.data = self.ps.getDataV(channel, actual_num_samples)

    def run_block(self):

        """Démarre une acquisition en mode 'Block'"""

        self.ps.runBlock()

    def wait_ready(self):
        
        """Attend que l'acquisition soit terminée"""

        self.ps.waitReady()

    def close_scope(self):

        """Arrête l'oscilloscope et libère ses ressources"""

        self.ps.stop()
        self.ps.close()

    def get_plot(self, type='A'):

        """Émet les données via le signal current_plot pour mise à jour dans l'interface graphique"""
        
        self.run_block()
        self.wait_ready()
        # self.data_all_channels = []
        # for i in ['A', 'B', 'C', 'D']:
        #     self.get_data(i)
        #     self.data_all_channels.append(self.data)
        # self.current_plot.emit(self.time, self.data_all_channels)
        self.plot = []
        self.get_data(type)
        self.plot.append(self.data)
        self.current_plot.emit(self.time, self.plot)



if __name__ == '__main__':
    import time
    dataTimeAxis = 0
    data = []
    block = BlockMode()
    block.set_channels('A')
    block.set_sampling()
    block.set_sig_gen()
    start = time.time()
    data = []
    t = []
    trigger_level = 0.5
    start = time.time()
    for i in range(0, 5):
        block.set_triggers(threshold=trigger_level)
        block.run_block()
        block.wait_ready()
        block.get_data()
        t.append(np.arange(block.actual_num_samples) * block.actual_sampling_interval)
        data.append(block.data)
        trigger_level += 0.1
        # print(time.time() - start)
        print(data)
        #print(data[0])
        #print(data[1])
        block.ps.stop()
        # time.sleep()
    # block.close_scope()
    block.ps.close()