# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_code_av.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_code_av(object):
    def setupUi(self, Dialog_code_av):
        Dialog_code_av.setObjectName("Dialog_code_av")
        Dialog_code_av.resize(1021, 596)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_code_av)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(Dialog_code_av)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Codes")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_code_av)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play.setGeometry(QtCore.QRect(10, 30, 85, 27))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_stop.setGeometry(QtCore.QRect(100, 30, 85, 27))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalSlider_vol = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_vol.setGeometry(QtCore.QRect(795, 30, 160, 18))
        self.horizontalSlider_vol.setMaximum(100)
        self.horizontalSlider_vol.setProperty("value", 100)
        self.horizontalSlider_vol.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vol.setObjectName("horizontalSlider_vol")
        self.label_volume = QtWidgets.QLabel(self.groupBox_2)
        self.label_volume.setGeometry(QtCore.QRect(700, 30, 81, 20))
        self.label_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_volume.setObjectName("label_volume")
        self.label_time = QtWidgets.QLabel(self.groupBox_2)
        self.label_time.setGeometry(QtCore.QRect(400, 30, 231, 21))
        self.label_time.setObjectName("label_time")
        self.label_time_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_time_2.setGeometry(QtCore.QRect(740, 63, 231, 21))
        self.label_time_2.setObjectName("label_time_2")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 0, 1003, 23))
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton_coding = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_coding.setGeometry(QtCore.QRect(190, 30, 181, 27))
        self.pushButton_coding.setObjectName("pushButton_coding")
        self.label_code = QtWidgets.QLabel(self.groupBox_2)
        self.label_code.setGeometry(QtCore.QRect(400, 63, 331, 17))
        self.label_code.setObjectName("label_code")
        self.label_coder = QtWidgets.QLabel(self.groupBox_2)
        self.label_coder.setGeometry(QtCore.QRect(190, 63, 141, 17))
        self.label_coder.setObjectName("label_coder")
        self.pushButton_select = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_select.setGeometry(QtCore.QRect(10, 60, 171, 27))
        self.pushButton_select.setObjectName("pushButton_select")
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog_code_av)
        QtCore.QMetaObject.connectSlotsByName(Dialog_code_av)
        Dialog_code_av.setTabOrder(self.pushButton_play, self.pushButton_stop)
        Dialog_code_av.setTabOrder(self.pushButton_stop, self.horizontalSlider_vol)

    def retranslateUi(self, Dialog_code_av):
        _translate = QtCore.QCoreApplication.translate
        Dialog_code_av.setWindowTitle(_translate("Dialog_code_av", "Code Audio Video"))
        self.pushButton_play.setText(_translate("Dialog_code_av", "Play"))
        self.pushButton_stop.setText(_translate("Dialog_code_av", "Stop"))
        self.label_volume.setText(_translate("Dialog_code_av", "Volume"))
        self.label_time.setText(_translate("Dialog_code_av", "Time:"))
        self.label_time_2.setText(_translate("Dialog_code_av", "Duration: "))
        self.horizontalSlider.setToolTip(_translate("Dialog_code_av", "<html><head/><body><p>Left click on the slider button and drag left or right to change video position.</p></body></html>"))
        self.pushButton_coding.setToolTip(_translate("Dialog_code_av", "<html><head/><body><p>Select a code. Play video from start or another position. Press the Start coding button to begin coding the audio/video segement. Press the Stop coding button to end the coded segment.</p></body></html>"))
        self.pushButton_coding.setText(_translate("Dialog_code_av", "Start coding"))
        self.label_code.setText(_translate("Dialog_code_av", "Code:"))
        self.label_coder.setText(_translate("Dialog_code_av", "Coder:"))
        self.pushButton_select.setText(_translate("Dialog_code_av", "Select media"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_code_av = QtWidgets.QDialog()
    ui = Ui_Dialog_code_av()
    ui.setupUi(Dialog_code_av)
    Dialog_code_av.show()
    sys.exit(app.exec_())

