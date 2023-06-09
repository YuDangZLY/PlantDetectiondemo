# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlantDocDetection_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1226, 769)
        MainWindow.setMinimumSize(QtCore.QSize(1226, 769))
        MainWindow.setMaximumSize(QtCore.QSize(1226, 769))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/count.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#centralwidget{\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralWidget{\n"
"    border-image: url(:/newPrefix/images_test/back-image.png);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(58, 155, 280, 35))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(150, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        self.label_objNum = QtWidgets.QLabel(self.centralwidget)
        self.label_objNum.setGeometry(QtCore.QRect(56, 342, 165, 39))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_objNum.setFont(font)
        self.label_objNum.setStyleSheet("color: #3a0088;")
        self.label_objNum.setObjectName("label_objNum")
        self.label_ymin = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin.setGeometry(QtCore.QRect(217, 648, 87, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_ymin.setFont(font)
        self.label_ymin.setStyleSheet("font: italic 12pt \"Consolas\";\n"
"color: #930077;")
        self.label_ymin.setObjectName("label_ymin")
        self.label_ymax_result = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax_result.setGeometry(QtCore.QRect(306, 682, 87, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(12)
        self.label_ymax_result.setFont(font)
        self.label_ymax_result.setStyleSheet("color: #3a0088;")
        self.label_ymax_result.setObjectName("label_ymax_result")
        self.label_numer_result = QtWidgets.QLabel(self.centralwidget)
        self.label_numer_result.setGeometry(QtCore.QRect(244, 340, 155, 37))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(16)
        self.label_numer_result.setFont(font)
        self.label_numer_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_numer_result.setObjectName("label_numer_result")
        self.label_conf = QtWidgets.QLabel(self.centralwidget)
        self.label_conf.setGeometry(QtCore.QRect(56, 522, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_conf.setFont(font)
        self.label_conf.setStyleSheet("color: #3a0088;")
        self.label_conf.setObjectName("label_conf")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 40, 1201, 75))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("QLabel{\n"
"color: #e61c5d;\n"
"font:  20pt \"楷体\";\n"
"}")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_picNumber = QtWidgets.QLabel(self.centralwidget)
        self.label_picNumber.setGeometry(QtCore.QRect(8, 340, 45, 45))
        self.label_picNumber.setStyleSheet("border-image: url(:/images/icons/count.png);")
        self.label_picNumber.setText("")
        self.label_picNumber.setObjectName("label_picNumber")
        self.comboBox_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_select.setGeometry(QtCore.QRect(56, 426, 169, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.comboBox_select.setFont(font)
        self.comboBox_select.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox_select.setStyleSheet("color: rgb(43, 89, 124);\n"
"font: italic 12pt \"Consolas\";")
        self.comboBox_select.setIconSize(QtCore.QSize(36, 36))
        self.comboBox_select.setObjectName("comboBox_select")
        self.comboBox_select.addItem("")
        self.label_xmax = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax.setGeometry(QtCore.QRect(14, 682, 83, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_xmax.setFont(font)
        self.label_xmax.setStyleSheet("font: italic 12pt \"Consolas\";\n"
"color: #930077;")
        self.label_xmax.setObjectName("label_xmax")
        self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_camera.setGeometry(QtCore.QRect(892, 155, 280, 35))
        self.textEdit_camera.setMinimumSize(QtCore.QSize(150, 30))
        self.textEdit_camera.setMaximumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_camera.setFont(font)
        self.textEdit_camera.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_camera.setReadOnly(True)
        self.textEdit_camera.setObjectName("textEdit_camera")
        self.label_xmin_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin_result.setGeometry(QtCore.QRect(96, 648, 81, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(12)
        self.label_xmin_result.setFont(font)
        self.label_xmin_result.setStyleSheet("color: #3a0088;")
        self.label_xmin_result.setObjectName("label_xmin_result")
        self.label_score_result = QtWidgets.QLabel(self.centralwidget)
        self.label_score_result.setGeometry(QtCore.QRect(154, 518, 253, 47))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(16)
        self.label_score_result.setFont(font)
        self.label_score_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_score_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score_result.setObjectName("label_score_result")
        self.label_location = QtWidgets.QLabel(self.centralwidget)
        self.label_location.setGeometry(QtCore.QRect(58, 600, 157, 41))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_location.setFont(font)
        self.label_location.setStyleSheet("color: #3a0088;")
        self.label_location.setObjectName("label_location")
        self.label_picConf = QtWidgets.QLabel(self.centralwidget)
        self.label_picConf.setGeometry(QtCore.QRect(10, 524, 40, 40))
        self.label_picConf.setStyleSheet("border-image: url(:/images/icons/Score.png);")
        self.label_picConf.setText("")
        self.label_picConf.setObjectName("label_picConf")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(410, 256, 806, 454))
        self.label_display.setMinimumSize(QtCore.QSize(806, 454))
        self.label_display.setMaximumSize(QtCore.QSize(1152, 648))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_display.setFont(font)
        self.label_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_display.setStyleSheet("border-image: url(:/UI_rec/icons/ini-image1.png);")
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.label_xmax_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax_result.setGeometry(QtCore.QRect(96, 682, 89, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(12)
        self.label_xmax_result.setFont(font)
        self.label_xmax_result.setStyleSheet("color: #3a0088;")
        self.label_xmax_result.setObjectName("label_xmax_result")
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(10, 284, 40, 40))
        self.label_picTime.setStyleSheet("border-image: url(:/images/icons/net_speed.png);")
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1, 562, 409, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_ymax = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax.setGeometry(QtCore.QRect(217, 682, 89, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_ymax.setFont(font)
        self.label_ymax.setStyleSheet("font: italic 12pt \"Consolas\";\n"
"color: #930077;")
        self.label_ymax.setObjectName("label_ymax")
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(7, 150, 45, 45))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/recovery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon1)
        self.toolButton_file.setIconSize(QtCore.QSize(37, 37))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_file")
        self.textEdit_video = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_video.setGeometry(QtCore.QRect(482, 154, 281, 35))
        self.textEdit_video.setMinimumSize(QtCore.QSize(150, 30))
        self.textEdit_video.setMaximumSize(QtCore.QSize(340, 40))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_video.setFont(font)
        self.textEdit_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_video.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_video.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_video.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_video.setReadOnly(True)
        self.textEdit_video.setObjectName("textEdit_video")
        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(840, 150, 45, 45))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon2)
        self.toolButton_camera.setIconSize(QtCore.QSize(37, 37))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(2, 242, 407, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_time_result = QtWidgets.QLabel(self.centralwidget)
        self.label_time_result.setGeometry(QtCore.QRect(176, 284, 129, 37))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_time_result.setFont(font)
        self.label_time_result.setStyleSheet("color: #3a0088;")
        self.label_time_result.setObjectName("label_time_result")
        self.label_picSelect = QtWidgets.QLabel(self.centralwidget)
        self.label_picSelect.setGeometry(QtCore.QRect(12, 422, 35, 35))
        self.label_picSelect.setStyleSheet("border-image: url(:/images/icons/selection.png);")
        self.label_picSelect.setText("")
        self.label_picSelect.setObjectName("label_picSelect")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(2, 380, 407, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.toolButton_saveing = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_saveing.setGeometry(QtCore.QRect(11, 9, 31, 27))
        self.toolButton_saveing.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_saveing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_saveing.setAutoFillBackground(False)
        self.toolButton_saveing.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_saveing.setIcon(icon3)
        self.toolButton_saveing.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_saveing.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_saveing.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_saveing.setAutoRaise(False)
        self.toolButton_saveing.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_saveing.setObjectName("toolButton_saveing")
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setGeometry(QtCore.QRect(56, 476, 113, 37))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_class.setFont(font)
        self.label_class.setStyleSheet("color: #3a0088;")
        self.label_class.setObjectName("label_class")
        self.label_xmin = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin.setGeometry(QtCore.QRect(14, 648, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_xmin.setFont(font)
        self.label_xmin.setStyleSheet("font: italic 12pt \"Consolas\";\n"
"color: #930077;")
        self.label_xmin.setObjectName("label_xmin")
        self.toolButton_video = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_video.setGeometry(QtCore.QRect(430, 150, 45, 45))
        self.toolButton_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_video.setAutoFillBackground(False)
        self.toolButton_video.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_video.setIcon(icon4)
        self.toolButton_video.setIconSize(QtCore.QSize(37, 37))
        self.toolButton_video.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_video.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_video.setAutoRaise(False)
        self.toolButton_video.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_video.setObjectName("toolButton_video")
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(14, 478, 35, 35))
        self.label_picResult.setStyleSheet("border-image: url(:/images/icons/result.png);")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        self.label_picLocation = QtWidgets.QLabel(self.centralwidget)
        self.label_picLocation.setGeometry(QtCore.QRect(12, 598, 35, 35))
        self.label_picLocation.setStyleSheet("border-image: url(:/images/icons/Ordinateur.png);")
        self.label_picLocation.setText("")
        self.label_picLocation.setObjectName("label_picLocation")
        self.label_ymin_result = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin_result.setGeometry(QtCore.QRect(306, 648, 75, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(12)
        self.label_ymin_result.setFont(font)
        self.label_ymin_result.setStyleSheet("color: #3a0088;")
        self.label_ymin_result.setObjectName("label_ymin_result")
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(58, 282, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_useTime.setFont(font)
        self.label_useTime.setStyleSheet("color: #3a0088;")
        self.label_useTime.setObjectName("label_useTime")
        self.label_class_result = QtWidgets.QLabel(self.centralwidget)
        self.label_class_result.setGeometry(QtCore.QRect(156, 470, 249, 47))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(16)
        self.label_class_result.setFont(font)
        self.label_class_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_class_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_class_result.setObjectName("label_class_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plant Detection"))
        self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择图片文件</span></p></body></html>"))
        self.label_objNum.setText(_translate("MainWindow", "目标数目:"))
        self.label_ymin.setText(_translate("MainWindow", "ymin: "))
        self.label_ymax_result.setText(_translate("MainWindow", "0"))
        self.label_numer_result.setText(_translate("MainWindow", "0"))
        self.label_conf.setText(_translate("MainWindow", "置信度:"))
        self.label_title.setToolTip(_translate("MainWindow", "<html><head/><body><p>yolov5</p><p>深度学习</p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "基于深度学习的作物检测与识别系统"))
        self.comboBox_select.setCurrentText(_translate("MainWindow", "所有目标"))
        self.comboBox_select.setItemText(0, _translate("MainWindow", "所有目标"))
        self.label_xmax.setText(_translate("MainWindow", "xmax: "))
        self.textEdit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">摄像头未开启</span></p></body></html>"))
        self.label_xmin_result.setText(_translate("MainWindow", "0"))
        self.label_score_result.setText(_translate("MainWindow", "0"))
        self.label_location.setText(_translate("MainWindow", "标记框:"))
        self.label_display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_xmax_result.setText(_translate("MainWindow", "0"))
        self.label_ymax.setText(_translate("MainWindow", "ymax: "))
        self.toolButton_file.setToolTip(_translate("MainWindow", "选择图片"))
        self.textEdit_video.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择视频文件</span></p></body></html>"))
        self.toolButton_camera.setToolTip(_translate("MainWindow", "开启摄像头"))
        self.label_time_result.setText(_translate("MainWindow", "0 s"))
        self.toolButton_saveing.setToolTip(_translate("MainWindow", "保存结果"))
        self.label_class.setText(_translate("MainWindow", "类型:"))
        self.label_xmin.setText(_translate("MainWindow", "xmin: "))
        self.toolButton_video.setToolTip(_translate("MainWindow", "选择视频"))
        self.label_ymin_result.setText(_translate("MainWindow", "0"))
        self.label_useTime.setText(_translate("MainWindow", "用时:"))
        self.label_class_result.setText(_translate("MainWindow", "无"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))
import RecSystem_rc
