import numpy as np
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button #, RadioButtons
import scipy.signal as ss

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
    """This function does blah blah."""
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("binary files",["*.bin","*.raw"]),("all files","*.*")))
    print(root.filename)
    

    # app = QtWidgets.QApplication(sys.argv)
    # window = SeeProcessing()
    # window.show()
    # app.exec_()
if __name__ == '__main__':
    main()