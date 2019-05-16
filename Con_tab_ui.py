# -*- coding: utf-8 -*-

"""
Module implementing Cal_Con.
"""

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene, QMessageBox, QFileDialog
import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rcParams['xtick.direction'] = 'in'  # 将x轴的刻度线设置为朝内
matplotlib.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度线设置为朝内
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
from math import sqrt, pi
from scipy import signal

from Ui_Con_tab_ui import Ui_Form
import sys


class Cal_Con(QWidget, Ui_Form):
    """
    1.激光脉冲分为‘矩形’脉冲和‘高斯脉冲’
    2.选通门为‘矩形’
    3.回波能量为激光脉冲和选通门的卷积
    4.改程序拥有显示和保存两种功能
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Cal_Con, self).__init__(parent)
        self.setupUi(self)

    def gate_function(self, x, a):
        """
        矩形函数
        """
        return [1 if (-a <= i <= a) else 0 for i in x]

    def gaussian(self, x, mu, sig):
        # 1. / (sqrt(2. * pi) * sig) 为尖峰的高度
        # mu为尖峰中心坐标
        # sig为标准方差，表征宽度
        return 1. / (sqrt(2. * pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.) / 2)

    @pyqtSlot()
    def on_Show_Gate_clicked(self):
        """
        生成选通门函数
        """
        try:
            self.gate_width = float(self.Set_Gate_Width.text())
            self.x_lim = np.arange(
                (-self.gate_width), self.gate_width, step=0.1)
            self.gate = self.gate_function(
                self.x_lim, self.gate_width / 2)
            self.num_gate = len(self.x_lim)
            fig = Figure()
            self.ax_gate = fig.add_subplot(111)
            self.ax_gate.set_xlim([(-self.gate_width), self.gate_width])
            self.ax_gate.plot(self.x_lim, self.gate)
            self.ax_gate.set_xlabel('T/ns')
            self.ax_gate.set_ylabel('Normalizated Volts/mJ')
            self.ax_gate.set_title('Gate')
            self.ax_gate.text(-self.gate_width / 4, 0.8,
                              'Gate Width %s ns' % self.gate_width)
            dr = FigureCanvas(fig)
            graphicscene = QGraphicsScene()
            graphicscene.addWidget(dr)
            self.GraphicsView_Gate.setScene(graphicscene)
            self.GraphicsView_Gate.show()
        except:
            QMessageBox.information(self, '错误', '请输入选通门宽度', QMessageBox.Ok)

    @pyqtSlot()
    def on_Save_Gate_clicked(self):
        """
        保存生成的选通门图像
        """
        try:
            file_path = QFileDialog.getSaveFileName(
                self, 'save file', 'C:\\Users\\Sai\\Desktop', 'image files(*.jpg *.bmp)')[0]
            saving = self.ax_gate.figure.savefig(file_path, dpi=600)
            if saving == None:
                QMessageBox.information(self, '提示', '保存选通门成功', QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '保存选通门失败', QMessageBox.Ok)
        except AttributeError:
            QMessageBox.information(self, '错误', '请先生成选通门宽', QMessageBox.Ok)

    @pyqtSlot()
    def on_Show_Laser_clicked(self):
        """
        根据所选择的tabwidget ID来确定是生成矩形脉冲还是高斯脉冲
        """
        try:
            self.index = self.tabWidget.currentIndex()
            if self.index == 0: # 将激光脉冲看作矩形函数
                self.num_laser = len(self.x_lim)
                self.laser_width = float(self.Set_Laser_Width.text())
                self.laser = self.gate_function(
                    self.x_lim, self.laser_width / 2)
                fig = Figure()
                self.ax_laser = fig.add_subplot(111)
                self.ax_laser.set_xlim([(-self.gate_width), self.gate_width])
                self.ax_laser.set_xlim([0, 1])
                self.ax_laser.cla()  # 清除坐标轴
                self.ax_laser.plot(self.x_lim, self.laser)
                self.ax_laser.set_xlabel('T/ns')
                self.ax_laser.set_ylabel('Normalizated Energy/mJ')
                self.ax_laser.set_title('Laser Pulse')
                self.ax_laser.text(-self.laser_width / 4, 0.8,
                                   'Laser Width %s ns' % self.laser_width)

                dr = FigureCanvas(fig)
                graphicscene_laser = QGraphicsScene()
                graphicscene_laser.addWidget(dr)
                self.GraphicsView_Laser.setScene(graphicscene_laser)
                self.GraphicsView_Laser.show()
            elif self.index == 1: # 将激光脉冲看作高斯脉冲
                self.miu = 0
                self.laser_width = float(self.Set_Sigma.text())
                self.num_laser = len(self.x_lim)
                self.laser_no = self.gaussian(
                    self.x_lim, self.miu, self.laser_width)
                self.laser = (self.laser_no - self.laser_no.min()) / \
                    (self.laser_no.max() - self.laser_no.min())
                fig = Figure()
                self.ax_laser = fig.add_subplot(111)
                self.ax_laser.set_xlim([(-self.gate_width), self.gate_width])
                self.ax_laser.set_xlim([0, 1])
                self.ax_laser.cla()  # 清除坐标轴
                self.ax_laser.plot(self.x_lim, self.laser)
                self.ax_laser.set_xlabel('T/ns')
                self.ax_laser.set_ylabel('Normalizated Energy/mJ')
                self.ax_laser.set_title('Laser Pulse')
                self.ax_laser.text(-self.miu, self.laser.max() / 2,
                                   'Laser Width %s ns' % self.laser_width)
                dr = FigureCanvas(fig)
                graphicscene_laser = QGraphicsScene()
                graphicscene_laser.addWidget(dr)
                self.GraphicsView_Laser.setScene(graphicscene_laser)
                self.GraphicsView_Laser.show()
        except:
            QMessageBox.information(self, '错误', '请输入激光脉冲宽度', QMessageBox.Ok)

    @pyqtSlot()
    def on_Save_Laser_clicked(self):
        """
        保存生成的激光脉冲
        """
        try:
            file_path = QFileDialog.getSaveFileName(
                self, 'save file', 'C:\\Users\\Sai\\Desktop', 'image files(*.jpg *.bmp)')[0]
            saving = self.ax_laser.figure.savefig(file_path, dpi=600)
            if saving == None:
                QMessageBox.information(self, '提示', '保存激光脉宽成功', QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '保存激光失败', QMessageBox.Ok)
        except AttributeError:
            QMessageBox.information(self, '错误', '请先生成激光脉宽', QMessageBox.Ok)

    @pyqtSlot()
    def on_Show_Res_clicked(self):
        """
        显示回波能量
        """
        try:
            num = self.num_gate + self.num_laser - 1
            con_result = signal.convolve(self.laser, self.gate, mode='full')
            res = (con_result - con_result.min()) / \
                (con_result.max() - con_result.min())
            x = np.linspace(- (self.laser_width + self.gate_width),
                            (self.laser_width + self.gate_width), num)
            fig = Figure()
            self.ax_res = fig.add_subplot(111)
            self.ax_res.set_xlim([- (self.laser_width + self.gate_width),
                                  (self.laser_width + self.gate_width)])
            self.ax_res.plot(x, res)
            self.ax_res.set_xlabel('T/ns')
            self.ax_res.set_ylabel('Normalizated Energy/mJ')
            self.ax_res.set_title('Echo Energy Envelope')
            dr = FigureCanvas(fig)
            graphicscene = QGraphicsScene()
            graphicscene.addWidget(dr)
            self.GraphicsView_Res.setScene(graphicscene)
            self.GraphicsView_Res.show()

        except:
            QMessageBox.information(
                self, '错误', '请先输入激光宽度和选通门宽度', QMessageBox.Ok)


    @pyqtSlot()
    def on_Save_Res_clicked(self):
        """
        保存生成的回波能量
        """
        try:
            file_path = QFileDialog.getSaveFileName(
                self, 'save file', 'C:\\Users\\Sai\\Desktop', 'image files(*.jpg *.bmp)')[0]
            saving = self.ax_res.figure.savefig(file_path, dpi=600)
            if saving == None:
                QMessageBox.information(self, '提示', '保存卷积结果成功', QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '保存卷积结果失败', QMessageBox.Ok)
        except AttributeError:
            QMessageBox.information(self, '错误', '请先生成卷积结果', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mytest = Cal_Con()

    mytest.show()
    app.exec_()
