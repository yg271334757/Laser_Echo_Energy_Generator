# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sai\Desktop\Con_New\Con_tab_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(995, 706)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.Rect_Laser = QtWidgets.QWidget()
        self.Rect_Laser.setObjectName("Rect_Laser")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Rect_Laser)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Set_Laser_Width = QtWidgets.QLineEdit(self.Rect_Laser)
        self.Set_Laser_Width.setObjectName("Set_Laser_Width")
        self.horizontalLayout_2.addWidget(self.Set_Laser_Width)
        self.tabWidget.addTab(self.Rect_Laser, "")
        self.Gauss_Laser = QtWidgets.QWidget()
        self.Gauss_Laser.setObjectName("Gauss_Laser")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Gauss_Laser)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Set_Miu = QtWidgets.QLineEdit(self.Gauss_Laser)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Set_Miu.sizePolicy().hasHeightForWidth())
        self.Set_Miu.setSizePolicy(sizePolicy)
        self.Set_Miu.setObjectName("Set_Miu")
        self.horizontalLayout.addWidget(self.Set_Miu)
        self.Set_Gas_Width = QtWidgets.QLineEdit(self.Gauss_Laser)
        self.Set_Gas_Width.setObjectName("Set_Gas_Width")
        self.horizontalLayout.addWidget(self.Set_Gas_Width)
        self.Set_Sigma = QtWidgets.QLineEdit(self.Gauss_Laser)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Set_Sigma.sizePolicy().hasHeightForWidth())
        self.Set_Sigma.setSizePolicy(sizePolicy)
        self.Set_Sigma.setObjectName("Set_Sigma")
        self.horizontalLayout.addWidget(self.Set_Sigma)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.Gauss_Laser, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.Show_Laser = QtWidgets.QPushButton(Form)
        self.Show_Laser.setObjectName("Show_Laser")
        self.horizontalLayout_4.addWidget(self.Show_Laser)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.GraphicsView_Laser = QtWidgets.QGraphicsView(Form)
        self.GraphicsView_Laser.setObjectName("GraphicsView_Laser")
        self.verticalLayout.addWidget(self.GraphicsView_Laser)
        self.Save_Laser = QtWidgets.QPushButton(Form)
        self.Save_Laser.setObjectName("Save_Laser")
        self.verticalLayout.addWidget(self.Save_Laser)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Set_Gate_Width = QtWidgets.QLineEdit(Form)
        self.Set_Gate_Width.setObjectName("Set_Gate_Width")
        self.horizontalLayout_5.addWidget(self.Set_Gate_Width)
        self.Show_Gate = QtWidgets.QPushButton(Form)
        self.Show_Gate.setObjectName("Show_Gate")
        self.horizontalLayout_5.addWidget(self.Show_Gate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.GraphicsView_Gate = QtWidgets.QGraphicsView(Form)
        self.GraphicsView_Gate.setObjectName("GraphicsView_Gate")
        self.verticalLayout_2.addWidget(self.GraphicsView_Gate)
        self.Save_Gate = QtWidgets.QPushButton(Form)
        self.Save_Gate.setObjectName("Save_Gate")
        self.verticalLayout_2.addWidget(self.Save_Gate)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Show_Res = QtWidgets.QPushButton(Form)
        self.Show_Res.setObjectName("Show_Res")
        self.verticalLayout_3.addWidget(self.Show_Res)
        self.GraphicsView_Res = QtWidgets.QGraphicsView(Form)
        self.GraphicsView_Res.setObjectName("GraphicsView_Res")
        self.verticalLayout_3.addWidget(self.GraphicsView_Res)
        self.Save_Res = QtWidgets.QPushButton(Form)
        self.Save_Res.setObjectName("Save_Res")
        self.verticalLayout_3.addWidget(self.Save_Res)
        self.Quit_Button = QtWidgets.QPushButton(Form)
        self.Quit_Button.setObjectName("Quit_Button")
        self.verticalLayout_3.addWidget(self.Quit_Button)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.Quit_Button.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Set_Laser_Width.setToolTip(_translate("Form", "11111"))
        self.Set_Laser_Width.setPlaceholderText(
            _translate("Form", "请输入矩形激光脉宽,精确到0.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Rect_Laser), _translate("Form", "矩形激光脉冲"))
        self.Set_Miu.setPlaceholderText(_translate("Form", "设置中心位置"))
        self.Set_Gas_Width.setPlaceholderText(
            _translate("Form", "设置图像宽度,精确到0.1"))
        self.Set_Sigma.setPlaceholderText(_translate("Form", "设置高斯脉冲宽度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Gauss_Laser), _translate("Form", "高斯激光脉冲"))
        self.Show_Laser.setText(_translate("Form", "生成激光脉冲"))
        self.Save_Laser.setText(_translate("Form", "保存激光脉冲"))
        self.Set_Gate_Width.setPlaceholderText(_translate("Form", "请输入选通门宽"))
        self.Show_Gate.setText(_translate("Form", "生成选通门"))
        self.Save_Gate.setText(_translate("Form", "保存选通门"))
        self.Show_Res.setText(_translate("Form", "显示回波能量包络"))
        self.Save_Res.setText(_translate("Form", "保存回波能量包络"))
        self.Quit_Button.setText(_translate("Form", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
