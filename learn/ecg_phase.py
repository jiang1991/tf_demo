#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ecg obj
class Ecg(object):

    def __init__(self, buf):

        valueStruct = struct.unpack('<HI4H', buf[0:14])

        # total time length of the ecg data
        self.time_length = int(valueStruct[0] / 2)
        # HR result
        self.hr = valueStruct[2]
        # ST result
        self.st = valueStruct[3]
        # QRS result
        self.qrs = valueStruct[4]
        # PVCs result
        self.pvcs = valueStruct[5]

        self.datalength = int((valueStruct[1] - 2) / 2)

        # HRs, list of HR per second
        self.hrs = struct.unpack('<{lg}H'.format(lg=self.time_length), buf[21: 21+self.time_length*2])

        # ECG waveform data
        self.waveform = struct.unpack('<{length}h'.format(length=self.datalength), buf[21 + 2*self.time_length:21 + 10000 + 2*self.time_length])


# read raw data
def load_data():
    with open('./ecg/20190114111554', 'rb') as f:
        return f.read()


if __name__ == '__main__':

    buf = load_data()
    ecg = Ecg(buf)

    t = np.arange(0.0, ecg.datalength, 1)
    s = ecg.waveform

    fig, ax = plt.subplots()
    ax.plot(t, s)

    plt.show()
