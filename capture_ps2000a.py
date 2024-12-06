'''
This Program made to take a capture of picoscope2000Series depending on the mode considered

'''

import time
import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import QtCore

from ps2000a import PS2000a

class BlockMode(QtCore.QObject):

    current_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, parent=None):
        super().__init__(parent)  
        self.ps = PS2000a()

    def set_sampling(self, obs_duration=150e-6, num_samples = 4096):
        self.obs_duration = obs_duration
        self.num_samples = num_samples
        self.sampling_interval = self.obs_duration / self.num_samples
        self.actual_sampling_interval, self.actual_num_samples, self.max_samples = self.ps.setSamplingInterval(
            self.sampling_interval, self.obs_duration)
        self.time = np.arange(self.actual_num_samples) * self.actual_sampling_interval

    def set_channels(self,
                     channel='A',
                     coupling='DC',
                     vrange=2.0,
                     offset=0.0,
                     enabled=True,
                     BWLimited=False):
        self.ps.setChannel(channel, coupling, vrange, offset, enabled,
                           BWLimited)

    def set_triggers(self,
                     trig_src='A',
                     threshold=0.5,
                     direction='Falling',
                     delay=0,
                     timeout_ms=100,
                     enabled=True):
        self.ps.setSimpleTrigger(trig_src, threshold, direction, delay,
                                 timeout_ms, enabled)

    def set_sig_gen(self,
                    offsetVoltage=0,
                    pkToPk=2.0,
                    waveType="Sine",
                    frequency=50E3):
        self.ps.setSigGenBuiltInSimple(offsetVoltage, pkToPk, waveType,
                                       frequency)

    def get_data(self, channel='A', actual_num_samples=0):
        self.data = self.ps.getDataV(channel, actual_num_samples)

    def run_block(self):
        self.ps.runBlock()

    def wait_ready(self):
        self.ps.waitReady()

    def close_scope(self):
        self.ps.stop()
        self.ps.close()

    def get_plot(self, type='A'):
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