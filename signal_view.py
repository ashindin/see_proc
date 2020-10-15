import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button #, RadioButtons
import scipy.signal as ss

from binary_file_options import Ui_MainWindow

def get_raw_data_from_binary_file(fname,offset_samples,duration_samples,bit_depth,num_of_channels):
    f=open(fname,'rb')
    offset_bytes=offset_samples*(bit_depth//8)*num_of_channels
#     print(offset_bytes)
    f.seek(offset_bytes,0)
    data_raw=f.read(int(duration_samples*int(bit_depth/8)*num_of_channels))
    f.close()
    return data_raw
def raw_to_complex_volts(data_raw,nc,v_range,bit_depth=16):
    if bit_depth==16:
        data=np.fromstring(data_raw,dtype=np.int16)
        data=np.reshape(data,(nc,int(len(data_raw)/nc/2)),'F')*v_range/32767
        data_complex=np.zeros((int(nc/2),int(len(data_raw)/nc/2)),dtype=np.complex128)
        for i in range(int(nc/2)):
            data_complex[i,:]=data[2*i,:]+1j*data[2*i+1,:]
    elif bit_depth==32:
        data=np.fromstring(data_raw,dtype=np.int32)
        data=np.reshape(data,(nc,int(len(data_raw)/nc/4)),'F')*v_range/2147483647
        data_complex=np.zeros((int(nc/2),int(len(data_raw)/nc/4)),dtype=np.complex128)
        for i in range(int(nc/2)):
            data_complex[i,:]=data[2*i,:]+1j*data[2*i+1,:]
    return data_complex


def main():    

    app = QtWidgets.QApplication(sys.argv)
    fname = QtWidgets.QFileDialog.getOpenFileName(None, "Load binary file:", "", "Binary files (*.bin *.raw);; All files (*.*)")
    print(fname)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # app = QtWidgets.QApplication(sys.argv)
    # window = SeeProcessing()
    # window.show()
    # app.exec_()

    sys.exit(app.exec_())
if __name__ == '__main__':
    main()