"""This module does blah blah."""
import sys
from PyQt5 import QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from see_proc_gui import Ui_MainWindow

class SeeProcessing(QtWidgets.QMainWindow, Ui_MainWindow):
    """This class does blah blah."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        win = pg.GraphicsLayout()
        self.p0_plot = win.addPlot()
        self.p0_plot.setMaximumWidth(250)
        self.p0_plot.showGrid(x=True, y=True)
        self.p1_plot = win.addPlot()
        self.img = pg.ImageItem()
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.img)
        self.p1_plot.addItem(self.img)
        win.addItem(self.hist)
        self.p2_plot = win.addPlot(row=1, col=1, colspan=1)
        self.p2_plot.setMaximumHeight(200)
        self.p2_plot.showGrid(x=True, y=True)
        self.p3_plot = win.addPlot(row=1, col=0)
        self.p3_plot.setMaximumWidth(250)
        self.p3_plot.setMaximumHeight(200)
        self.p3_plot.setXRange(0, 1)
        self.p3_plot.setYRange(0, 1)
        self.text1 = pg.TextItem((str("ver: ")))
        self.p3_plot.addItem(self.text1)
        self.text1.setPos(0.1, 0.95)
        self.text2 = pg.TextItem((str("hor: ")))
        self.p3_plot.addItem(self.text2)
        self.text2.setPos(0.5, 0.95)
        self.text3 = pg.TextItem((str("")))
        self.text3.setPos(0.1, 0.7)
        self.p3_plot.addItem(self.text3)
        self.p3_plot.setMouseEnabled(x=False, y=False)
        self.p3_plot.hideAxis('bottom')
        self.p3_plot.hideAxis('left')
        pg.setConfigOptions(imageAxisOrder='row-major')
        self.graphicsView_lay.setCentralItem(win)
        self.p0_plot.setYLink(self.p1_plot)
        self.p2_plot.setXLink(self.p1_plot)
        # Создаем линии сечений
        self.ver_sec_line = self.p0_plot.plot([], []) # вертикальное сечение на p0_plot
        self.hor_sec_line = self.p2_plot.plot([], []) # горизонтальное сечение на p2_plot
        self.sec_line_hor = pg.InfiniteLine(angle=0, movable=True, pen='k')
        self.sec_line_ver = pg.InfiniteLine(angle=90, movable=True, pen='k')
        self.p1_plot.addItem(self.sec_line_hor)
        self.p1_plot.addItem(self.sec_line_ver)
        # Создаем BUM ROI
        bum_roi = [[5732, 10], [5733, 27], [5759, 55], [5795, 80], [5814, 91],
                   [5822, 74], [5820, 45], [5756, 15]]
        bum2_roi = [[5742, 52], [5751, 83], [5772, 121], [5791, 135],
                    [5795, 108], [5780, 69], [5749, 41]]
        bumd_roi = [[5774, 24], [5797, 44], [5824, 63], [5831, 45], [5809, 28],
                    [5775, 14]]
        dm_roi = [[5730, -12], [5730, -8], [5930, -8], [5930, -12]]
        um_roi = [[5730, 6], [5730, 11], [5930, 12], [5930, 6]]
        self.roi_bum_obj = pg.PolyLineROI(bum_roi, pen=(6, 9), closed=True,
                                          movable=False)
        self.roi_bum2_obj = pg.PolyLineROI(bum2_roi, pen=(6, 9), closed=True,
                                           movable=False)
        self.roi_bumd_obj = pg.PolyLineROI(bumd_roi, pen=(6, 9), closed=True,
                                           movable=False)
        self.roi_um_obj = pg.PolyLineROI(um_roi, pen=(6, 9), closed=True,
                                         movable=False)
        self.roi_dm_obj = pg.PolyLineROI(dm_roi, pen=(6, 9), closed=True,
                                         movable=False)
        self.f_axe = np.zeros(1)
        self.t_axe = np.zeros(1)
        self.data = np.zeros(1)
        self.interference_mask = np.zeros(1, dtype='bool')
        f0_min_ind = np.where(np.abs(self.t_axe-f0_min) ==
                              np.min(np.abs(self.t_axe-f0_min)))[0][0]
        f0_max_ind = np.where(np.abs(self.t_axe-f0_max) ==
                              np.min(np.abs(self.t_axe-f0_max)))[0][0]
        t_axe_mask = self.t_axe[f0_min_ind:f0_max_ind]
        f_axe_mask = f_min+np.arange(0., 0.1*mask.shape[1], 0.1)
        bum_int = np.zeros(len(t_axe_mask))
        bum_f0 = np.copy(t_axe_mask)
        bum_freqs = np.zeros(len(t_axe_mask))
        for j in range(len(t_axe_mask)):
            bum_int[j] = np.max(mask[j, :])
            bum_freqs[j] = f_axe_mask[np.argmax(mask[j, :])]
        self.bum_int_line.setData(bum_f0, bum_int)
        self.bum_freqs_line.setData(bum_f0, bum_freqs)
        print("WOW")
        # ~ except:
            # ~ print("ERROR UPDATE BUM ROI")
    def update_roi_bum2(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, data, interference_mask
        # ~ try:
        mask = self.roi_bum2_obj.getArrayRegion(self.data*(1-self.interference_mask)- \
                                                200*self.interference_mask, self.img)
        mask[mask == 0.] = -200
        handles = self.roi_bum2_obj.getHandles()
        roi_xy = [[np.round(handle.pos()[0]),
                   np.round(handle.pos()[1]*10)/10] for handle in handles]
        roi_xya = np.array(roi_xy)
        f0_min = np.min(roi_xya[:, 0])
        f0_max = np.max(roi_xya[:, 0])
        f_min = np.min(roi_xya[:, 1])
#                f_max=np.max(roi_xya[:, 1])
        f0_min_ind = np.where(np.abs(self.t_axe-f0_min) == np.min(np.abs(self.t_axe-f0_min)))[0][0]
        f0_max_ind = np.where(np.abs(self.t_axe-f0_max) == np.min(np.abs(self.t_axe-f0_max)))[0][0]
        t_axe_mask = self.t_axe[f0_min_ind:f0_max_ind]
        f_axe_mask = f_min+np.arange(0., 0.1*mask.shape[1], 0.1)
        bum2_int = np.zeros(len(t_axe_mask))
        bum2_f0 = np.copy(t_axe_mask)
        bum2_freqs = np.zeros(len(t_axe_mask))
        for j in range(len(t_axe_mask)):
            bum2_int[j] = np.max(mask[j, :])
            bum2_freqs[j] = f_axe_mask[np.argmax(mask[j, :])]
        self.bum2_int_line.setData(bum2_f0, bum2_int)
        self.bum2_freqs_line.setData(bum2_f0, bum2_freqs)
        # ~ except:
            # ~ print("ERROR UPDATE BUM2 ROI")
    def update_roi_bumd(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, data, interference_mask
        # ~ try:
        mask = self.roi_bumd_obj.getArrayRegion(self.data*(1-self.interference_mask)- \
                                                200*self.interference_mask, self.img)
        mask[mask == 0.] = -200
        handles = self.roi_bumd_obj.getHandles()
        roi_xy = [[np.round(handle.pos()[0]),
                   np.round(handle.pos()[1]*10)/10] for handle in handles]
        roi_xya = np.array(roi_xy)
        f0_min = np.min(roi_xya[:, 0])
        f0_max = np.max(roi_xya[:, 0])
        f_min = np.min(roi_xya[:, 1])
#        f_max=np.max(roi_xya[:,1])
        f0_min_ind = np.where(np.abs(self.t_axe-f0_min) == np.min(np.abs(self.t_axe-f0_min)))[0][0]
        f0_max_ind = np.where(np.abs(self.t_axe-f0_max) == np.min(np.abs(self.t_axe-f0_max)))[0][0]
        t_axe_mask = self.t_axe[f0_min_ind:f0_max_ind]
        f_axe_mask = f_min+np.arange(0., 0.1*mask.shape[1], 0.1)
        bumd_int = np.zeros(len(t_axe_mask))
        bumd_f0 = np.copy(t_axe_mask)
        bumd_freqs = np.zeros(len(t_axe_mask))
        for j in range(len(t_axe_mask)):
            bumd_int[j] = np.max(mask[j, :])
            bumd_freqs[j] = f_axe_mask[np.argmax(mask[j, :])]
        self.bumd_int_line.setData(bumd_f0, bumd_int)
        self.bumd_freqs_line.setData(bumd_f0, bumd_freqs)
        # ~ except:
            # ~ print("ERROR UPDATE BUMD ROI")
    def update_roi_dm(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, data, interference_mask
        # ~ try:
        mask = self.roi_dm_obj.getArrayRegion(self.data*(1-self.interference_mask)- \
                                              200*self.interference_mask, self.img)
        mask[mask == 0.] = -200
        handles = self.roi_dm_obj.getHandles()
        roi_xy = [[np.round(handle.pos()[0]),
                   np.round(handle.pos()[1]*10)/10] for handle in handles]
        roi_xya = np.array(roi_xy)
        f0_min = np.min(roi_xya[:, 0])
        f0_max = np.max(roi_xya[:, 0])
        f_min = np.min(roi_xya[:, 1])
#                f_max=np.max(roi_xya[:,1])
        f0_min_ind = np.where(np.abs(self.t_axe-f0_min) == np.min(np.abs(self.t_axe-f0_min)))[0][0]
        f0_max_ind = np.where(np.abs(self.t_axe-f0_max) == np.min(np.abs(self.t_axe-f0_max)))[0][0]
        t_axe_mask = self.t_axe[f0_min_ind:f0_max_ind]
        f_axe_mask = f_min+np.arange(0., 0.1*mask.shape[1], 0.1)
        dm_int = np.zeros(len(t_axe_mask))
        dm_f0 = np.copy(t_axe_mask)
        dm_freqs = np.zeros(len(t_axe_mask))
        for j in range(len(t_axe_mask)):
            dm_int[j] = np.max(mask[j, :])
            dm_freqs[j] = f_axe_mask[np.argmax(mask[j, :])]
        self.dm_int_line.setData(dm_f0, dm_int)
        self.dm_freqs_line.setData(dm_f0, dm_freqs)
        # ~ except:
            # ~ print("ERROR UPDATE DM ROI")
    def update_roi_um(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, data, interference_mask
        # ~ try:
        mask = self.roi_um_obj.getArrayRegion(self.data*(1-self.interference_mask)- \
                                              200*self.interference_mask, self.img)
        mask[mask == 0.] = -200
        handles = self.roi_um_obj.getHandles()
        roi_xy = [[np.round(handle.pos()[0]),
                   np.round(handle.pos()[1]*10)/10] for handle in handles]
        roi_xya = np.array(roi_xy)
        f0_min = np.min(roi_xya[:, 0])
        f0_max = np.max(roi_xya[:, 0])
        f_min = np.min(roi_xya[:, 1])
#                f_max=np.max(roi_xya[:,1])
        f0_min_ind = np.where(np.abs(self.t_axe-f0_min) == np.min(np.abs(self.t_axe-f0_min)))[0][0]
        f0_max_ind = np.where(np.abs(self.t_axe-f0_max) == np.min(np.abs(self.t_axe-f0_max)))[0][0]
        t_axe_mask = self.t_axe[f0_min_ind:f0_max_ind]
        f_axe_mask = f_min+np.arange(0., 0.1*mask.shape[1], 0.1)
        um_int = np.zeros(len(t_axe_mask))
        um_f0 = np.copy(t_axe_mask)
        um_freqs = np.zeros(len(t_axe_mask))
        for j in range(len(t_axe_mask)):
            um_int[j] = np.max(mask[j, :])
            um_freqs[j] = f_axe_mask[np.argmax(mask[j, :])]
        self.um_int_line.setData(um_f0, um_int)
        self.um_freqs_line.setData(um_f0, um_freqs)
        # ~ except:
            # ~ print("ERROR UPDATE DM ROI")
    def updatesec_ver(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, data
        sec_value = self.sec_line_ver.value()
        # ~ try:
        if len(self.t_axe) > 1:
            if sec_value >= self.t_axe[0] and sec_value <= self.t_axe[-1]:
                t_ind = np.where(np.abs(self.t_axe-sec_value) == \
                                 np.min(np.abs(self.t_axe-sec_value)))[0][0]
                self.ver_sec_line.setData(self.data.T[:, t_ind], self.f_axe/1000)
                # ~ self.statusBar().showMessage("{:.2f}".format(t_axe[t_ind]))
                self.text1.setText("ver: "+"{:.2f}".format(self.t_axe[t_ind]))
        # ~ except:
            # ~ print("Init")
    def updatesec_hor(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, data
        sec_value = self.sec_line_hor.value()
        # ~ try:
        if len(self.f_axe) > 1:
            if sec_value >= self.f_axe[0]/1000 and sec_value <= self.f_axe[-1]/1000:
                f_ind = np.where(np.abs(self.f_axe/1000-sec_value) == \
                                 np.min(np.abs(self.f_axe/1000-sec_value)))[0][0]
                # ~ print(f_ind,f_axe[f_ind])
                self.hor_sec_line.setData(self.t_axe, self.data.T[f_ind, :])
                # ~ self.statusBar().showMessage("{:.2f}".format(f_axe[f_ind]/1000))
                self.text2.setText("hor: "+"{:.2f}".format(self.f_axe[f_ind]/1000))
            # ~ except:
                # ~ print("Init")
    def on_open_click(self):
        """This method does blah blah."""
        # ~ global f_axe, t_axe, filename
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "QFileDialog.getOpenFileName()", "", ";Numpy data files (*.npz)",
            options=options)
        if self.filename:
            print(self.filename)
            self.text3.setText(self.filename.split('/')[-1])            
            # Загрузка и отображение спектрограммы
            dic = np.load(self.filename)
            spectrogram = dic['spectrogram'].T
            self.f_axe = dic['f_axe']
            df_step = (self.f_axe[1]-self.f_axe[0])/1000
            self.t_axe = dic['t_axe']
            if self.t_axe[1] < self.t_axe[0]:
                self.t_axe = self.t_axe[-1::-1]
                spectrogram = np.fliplr(spectrogram)
            dt_step = self.t_axe[1]-self.t_axe[0]
            self.data = 10*np.log10(spectrogram.T)
            self.interference_mask = np.zeros(self.data.shape, dtype='bool')
            self.img.setImage(self.data*(1-self.interference_mask)-200*self.interference_mask, autoLevels=False)
            self.img.scale(dt_step, df_step)
            self.img.translate(self.t_axe[0], (self.f_axe[0]/1000-df_step)/df_step)
            self.hist.gradient.loadPreset('flame')
            self.hist.setLevels(-130, -80)
            # Линии сечений на спектрограмме
            self.sec_line_hor.setValue((self.f_axe[0]+self.f_axe[-1])/2000)
            self.sec_line_hor.setZValue(1000)
            self.sec_line_ver.setValue(self.t_axe[len(self.t_axe)//2])
            self.sec_line_ver.setZValue(1000)
            # Пределы осей
            self.p0_plot.setXRange(-130, -80)
            self.p0_plot.setYRange(self.f_axe[0]/1000, self.f_axe[-1]/1000)
            self.p2_plot.setYRange(-130, -80)
            self.p2_plot.setXRange(self.t_axe[0], self.t_axe[-1])
            self.updatesec_hor()
            self.updatesec_ver()
            # Рисуем и обновляем ROI
            if self.radio_bum.isChecked():
                self.p1_plot.addItem(self.roi_bum_obj)
                self.update_roi_bum()
            if self.radio_2bum.isChecked():
                self.p1_plot.addItem(self.roi_bum2_obj)
                self.update_roi_bum2()
            if self.radio_bumd.isChecked():
                self.p1_plot.addItem(self.roi_bumd_obj)
                self.update_roi_bumd()
            if self.radio_um.isChecked():
                self.p1_plot.addItem(self.roi_um_obj)
                self.update_roi_um()
            if self.radio_dm.isChecked():
                self.p1_plot.addItem(self.roi_dm_obj)
                self.update_roi_dm()
            # Пробуем открыть proc файл
            filename_load = 'proc_'+self.filename.split('_')[-2]+'.npz'
            # ~ try:
            filedata = np.load(filename_load)
            # ~ print(list(filedata.keys()))
            self.interference_mask = filedata['interference_mask']
            roi_bum_xy = filedata['roi_bum_xy']
            roi_bumd_xy = filedata['roi_bumd_xy']
            # ~ roi_bum2_xy = filedata['roi_bum2_xy']
            # ~ roi_um_xy = filedata['roi_um_xy']
            roi_dm_xy = filedata['roi_dm_xy']
            self.img.setImage(self.data*(1.-self.interference_mask)-200.*self.interference_mask, autoLevels=False)
            self.p1_plot.removeItem(self.roi_bum_obj)
            self.roi_bum_obj = pg.PolyLineROI(roi_bum_xy, pen=(6, 9), closed=True, movable=False)
            # ~ self.p1_plot.removeItem(self.roi_bum2_obj)
            # ~ self.roi_bum2_obj = pg.PolyLineROI(roi_bum2_xy, pen=(6, 9), closed=True, movable=False)
            self.p1_plot.removeItem(self.roi_bumd_obj)
            self.roi_bumd_obj = pg.PolyLineROI(roi_bumd_xy, pen=(6, 9), closed=True, movable=False)
            self.p1_plot.removeItem(self.roi_um_obj)
            # ~ self.roi_um_obj = pg.PolyLineROI(roi_um_xy, pen=(6, 9), closed=True, movable=False)
            # ~ self.p1_plot.removeItem(self.roi_dm_obj)
            self.roi_dm_obj = pg.PolyLineROI(roi_dm_xy, pen=(6, 9), closed=True, movable=False)
            if self.radio_bum.isChecked():
                self.p1_plot.addItem(self.roi_bum_obj)
                self.update_roi_bum()
            if self.radio_2bum.isChecked():
                self.p1_plot.addItem(self.roi_bumd_obj)
                self.update_roi_bum2()
            if self.radio_bumd.isChecked():
                self.p1_plot.addItem(self.roi_bumd_obj)
                self.update_roi_bumd()
            if self.radio_um.isChecked():
                self.p1_plot.addItem(self.roi_um_obj)
                self.update_roi_um()
            if self.radio_dm.isChecked():
                self.p1_plot.addItem(self.roi_dm_obj)
                self.update_roi_dm()
            self.updatesec_hor()
            self.updatesec_ver()
            # ~ except:
                # ~ print("Can not load proc file")
    def on_save_click(self):
        """This method does blah blah."""
        # ~ global interference_mask, filename
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        name = self.filename.split('/')[-1]
        # ~ ''.join(name.split('.')[0:-1])+'_proc.npz'
        filename_save, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "QFileDialog.getSaveFileName()",
            'proc_'+name.split('_')[-2]+'.npz',
            "Numpy data files (*.npz)", options=options)
        if filename_save:
            print(filename_save)
            handles_bum = self.roi_bum_obj.getHandles()
            roi_bum_xy = [[np.round(handle.pos()[0]),
                           np.round(handle.pos()[1])] for handle in handles_bum]
            handles_bum2 = self.roi_bum2_obj.getHandles()
            roi_bum2_xy = [[np.round(handle.pos()[0]),
                            np.round(handle.pos()[1])] for handle in handles_bum2]
            handles_bumd = self.roi_bumd_obj.getHandles()
            roi_bumd_xy = [[np.round(handle.pos()[0]),
                            np.round(handle.pos()[1])] for handle in handles_bumd]
            handles_dm = self.roi_dm_obj.getHandles()
            roi_dm_xy = [[np.round(handle.pos()[0]),
                          np.round(handle.pos()[1])] for handle in handles_dm]
            handles_um = self.roi_um_obj.getHandles()
            roi_um_xy = [[np.round(handle.pos()[0]),
                          np.round(handle.pos()[1])] for handle in handles_um]
            # ~ bum_f0, bum_int= bum_int_line.getData()
            # ~ bum_f0, bum_freqs= bum_freqs_line.getData()
            # ~ bum2_f0, bum2_int= bum2_int_line.getData()
            # ~ bum2_f0, bum2_freqs= bum2_freqs_line.getData()
            # ~ bumd_f0, bumd_int= bumd_int_line.getData()
            # ~ bumd_f0, bumd_freqs= bumd_freqs_line.getData()
            # ~ dm_f0, dm_int= dm_int_line.getData()
            # ~ dm_f0, dm_freqs= dm_freqs_line.getData()
            # ~ um_f0, um_int= um_int_line.getData()
            # ~ um_f0, um_freqs= um_freqs_line.getData()
            np.savez_compressed(filename_save, roi_bum_xy=roi_bum_xy,
                                roi_bum2_xy=roi_bum2_xy, roi_bumd_xy=roi_bumd_xy,
                                roi_dm_xy=roi_dm_xy, roi_um_xy=roi_um_xy,
                                interference_mask=self.interference_mask)
    def on_load_click(self):
        """This method does blah blah."""
        # ~ global interference_mask, roi_bum_obj
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename_load, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "QFileDialog.getOpenFileName()", "", ";Numpy data files (*.npz)",
            options=options)
        print(filename_load)
        filedata = np.load(filename_load)
        self.interference_mask = filedata['interference_mask']
        roi_bum_xy = filedata['roi_bum_xy']
        roi_bumd_xy = filedata['roi_bumd_xy']
        # ~ roi_bum2_xy = filedata['roi_bum2_xy']
        # ~ roi_um_xy = filedata['roi_um_xy']
        roi_dm_xy = filedata['roi_dm_xy']
        self.img.setImage(self.data*(1.-self.interference_mask)-200.*self.interference_mask, autoLevels=False)
        self.p1_plot.removeItem(self.roi_bum_obj)
        self.roi_bum_obj = pg.PolyLineROI(roi_bum_xy, pen=(6, 9), closed=True, movable=False)
        # ~ self.p1_plot.removeItem(self.roi_bum2_obj)
        # ~ self.roi_bum2_obj = pg.PolyLineROI(roi_bum2_xy, pen=(6, 9), closed=True, movable=False)
        self.p1_plot.removeItem(self.roi_bumd_obj)
        self.roi_bumd_obj = pg.PolyLineROI(roi_bumd_xy, pen=(6, 9), closed=True, movable=False)
        # ~ self.p1_plot.removeItem(self.roi_um_obj)
        # ~ self.roi_um_obj = pg.PolyLineROI(roi_um_xy, pen=(6, 9), closed=True, movable=False)
        self.p1_plot.removeItem(self.roi_dm_obj)
        self.roi_dm_obj = pg.PolyLineROI(roi_dm_xy, pen=(6, 9), closed=True, movable=False)
        if self.radio_bum.isChecked():
            self.p1_plot.addItem(self.roi_bum_obj)
            self.update_roi_bum()
        if self.radio_2bum.isChecked():
            self.p1_plot.addItem(self.roi_bumd_obj)
            self.update_roi_bum2()
        if self.radio_bumd.isChecked():
            self.p1_plot.addItem(self.roi_bumd_obj)
            self.update_roi_bumd()
        if self.radio_um.isChecked():
            self.p1_plot.addItem(self.roi_um_obj)
            self.update_roi_um()
        if self.radio_dm.isChecked():
            self.p1_plot.addItem(self.roi_dm_obj)
            self.update_roi_dm()
        self.updatesec_hor()
        self.updatesec_ver()
#            roi_bum_xy=filedata['roi_bum_xy']
#            roi_bum2_xy=filedata['roi_bum2_xy']
#            roi_bumd_xy=filedata['roi_bumd_xy']
#            roi_dm_xy=filedata['roi_dm_xy']
#            roi_um_xy=filedata['roi_um_xy']
        # ~ p1_plot.removeItem(roi_bum_obj);
        # ~ roi_bum_obj=None
        # ~ roi_bum_obj=pg.PolyLineROI(roi_bum_xy, pen=(6,9), closed=True, movable=False)
        # ~ p1_plot.addItem(roi_bum_obj);
        # ~ update_roi_bum()
        # ~ img.setImage(data*(1.-interference_mask)-200.*interference_mask, autoLevels=False)
    def mousemoved_p0(self, evt):
        """This method does blah blah."""
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.p0_plot.sceneBoundingRect().contains(pos):
            mouse_point = self.p0_plot.vb.mapSceneToView(pos)
            self.statusBar().showMessage(
                "{:.2f}".format(mouse_point.x())+" "+"{:.2f}".format(mouse_point.y()))
    def mousemoved_p2(self, evt):
        """This method does blah blah."""
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.p2_plot.sceneBoundingRect().contains(pos):
            mouse_point = self.p2_plot.vb.mapSceneToView(pos)
            self.statusBar().showMessage(
                str(int(mouse_point.x()))+" "+"{:.2f}".format(mouse_point.y()))
    def mousemoved_p1(self, evt):
        """This method does blah blah."""
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.p1_plot.sceneBoundingRect().contains(pos):
            mouse_point = self.p1_plot.vb.mapSceneToView(pos)
            self.statusBar().showMessage(
                str(int(mouse_point.x()))+" "+"{:.2f}".format(mouse_point.y()))
    def on_click(self, event):
        """This method does blah blah."""
        # ~ global t_axe, f_axe, interference_mask, data
        pos = event.scenePos()
        but = event.button()
        mod = event.modifiers()
        if self.p1_plot.sceneBoundingRect().contains(pos):
            x_var = int(self.p1_plot.vb.mapSceneToView(pos).x())
            y_var = int(self.p1_plot.vb.mapSceneToView(pos).y()*10)/10+0.1
            t_ind = np.where(np.abs(self.t_axe-x_var) == np.min(np.abs(self.t_axe-x_var)))[0][0]
            f_ind = np.where(np.abs(self.f_axe/1000-y_var) == \
                             np.min(np.abs(self.f_axe/1000-y_var)))[0][0]
            if mod == QtCore.Qt.ControlModifier:
                if but == 1:
                    self.interference_mask[t_ind, f_ind] = 1
                    print("Erase", x_var, "{:.1f}".format(y_var))
                elif but == 4:
                    self.interference_mask[t_ind, f_ind] = 0
                    print("Restore", x_var, "{:.1f}".format(y_var))
            if mod == QtCore.Qt.ShiftModifier:
                f_ind_shift = int(self.Text_box.text())
                if f_ind_shift != 0:
                    down_steps = f_ind//f_ind_shift
                    up_steps = (len(self.f_axe)-1-f_ind)//f_ind_shift
                    if but == 1:
                        print("Erase", x_var, "{:.1f}".format(y_var), " f_ind_shift=",
                              f_ind_shift)
                        for i in range(down_steps):
                            if t_ind+i < len(self.t_axe):
                                self.interference_mask[t_ind+i, f_ind-f_ind_shift*i] = 1
                        for i in range(up_steps):
                            if t_ind >= i:
                                self.interference_mask[t_ind-i, f_ind+f_ind_shift*i] = 1
                    elif but == 4:
                        print("Restore", x_var, "{:.1f}".format(y_var),
                              " f_ind_shift=", f_ind_shift)
                        for i in range(down_steps):
                            if t_ind+i < len(self.t_axe):
                                self.interference_mask[t_ind+i, f_ind-f_ind_shift*i] = 0
                        for i in range(up_steps):
                            if t_ind >= i:
                                self.interference_mask[t_ind-i, f_ind+f_ind_shift*i] = 0
                else:
                    if but == 1:
                        print("Erase", x_var, "{:.1f}".format(y_var), " f_ind_shift=", f_ind_shift)
                        self.interference_mask[:, f_ind] = 1
                    elif but == 4:
                        print("Restore", x_var, "{:.1f}".format(y_var),
                              " f_ind_shift=", f_ind_shift)
                        self.interference_mask[:, f_ind] = 0
            self.img.setImage(self.data*(1.-self.interference_mask)-200.*self.interference_mask, autoLevels=False)
            # ~ print(interference_mask.shape)
            if self.radio_bum.isChecked():
                self.update_roi_bum()
            if self.radio_2bum.isChecked():
                self.update_roi_bum2()
            if self.radio_bumd.isChecked():
                self.update_roi_bumd()
            if self.radio_um.isChecked():
                self.update_roi_um()
            if self.radio_dm.isChecked():
                self.update_roi_dm()
            self.updatesec_hor()
            self.updatesec_ver()
    def btnstate(self, but):
        """This method does blah blah."""
        if but.text() == "BUM":
            if but.isChecked():
                print(but.text()+" is selected")
                self.p1_plot.addItem(self.roi_bum_obj)
                self.bum_int_line.show()
                self.bum_freqs_line.show()
                self.update_roi_bum()
            else:
                print(but.text()+" is deselected")
                self.p1_plot.removeItem(self.roi_bum_obj)
                self.bum_int_line.hide()
                self.bum_freqs_line.hide()
        if but.text() == "2BUM":
            if but.isChecked():
                print(but.text()+" is selected")
                self.p1_plot.addItem(self.roi_bum2_obj)
                self.bum2_int_line.show()
                self.bum2_freqs_line.show()
                self.update_roi_bum2()
            else:
                print(but.text()+" is deselected")
                self.p1_plot.removeItem(self.roi_bum2_obj)
                self.bum2_int_line.hide()
                self.bum2_freqs_line.hide()
        if but.text() == "BUMD":
            if but.isChecked():
                print(but.text()+" is selected")
                self.p1_plot.addItem(self.roi_bumd_obj)
                self.bumd_int_line.show()
                self.bumd_freqs_line.show()
                self.update_roi_bumd()
            else:
                print(but.text()+" is deselected")
                self.p1_plot.removeItem(self.roi_bumd_obj)
                self.bumd_int_line.hide()
                self.bumd_freqs_line.hide()
        if but.text() == "DM":
            if but.isChecked():
                print(but.text()+" is selected")
                self.p1_plot.addItem(self.roi_dm_obj)
                self.dm_int_line.show()
                self.dm_freqs_line.show()
                self.update_roi_dm()
            else:
                print(but.text()+" is deselected")
                self.p1_plot.removeItem(self.roi_dm_obj)
                self.dm_int_line.hide()
                self.dm_freqs_line.hide()
        if but.text() == "UM":
            if but.isChecked():
                print(but.text()+" is selected")
                self.p1_plot.addItem(self.roi_um_obj)
                self.um_int_line.show()
                self.um_freqs_line.show()
                self.update_roi_um()
            else:
                print(but.text()+" is deselected")
                self.p1_plot.removeItem(self.roi_um_obj)
                self.um_int_line.hide()
                self.um_freqs_line.hide()
def main():
    """This function does blah blah."""
    app = QtWidgets.QApplication(sys.argv)
    window = SeeProcessing()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
    
