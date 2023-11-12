# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 300)
        MainWindow.setMinimumSize(QSize(350, 300))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/password_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"  	color: white;\n"
"  	background-color: #1d1d1d;\n"
"	font-family: Verdana;\n"
"	font-size: 12pt;\n"
"	margin: 0px;\n"
"}\n"
"QPushButton{\n"
"  border: 2px solid gray;\n"
"  border-radius: 4px;\n"
"  font-size: 14pt;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #242425;\n"
"  border: 2px solid #9184e0;\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #9184e0;\n"
"  border: 2px solid #9184e0;\n"
"  color: black\n"
"}\n"
"QPushButton:checked{\n"
"  background-color: #9184e0;\n"
"  border: 2px solid #9184e0;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton#btn_upper,#btn_special,#btn_num,#btn_lower{\n"
"	padding: 8px;\n"
"}\n"
"\n"
"QFrame{\n"
"  border: 2px solid gray;\n"
"  border-radius: 4px;\n"
"  margin-right: 0px;\n"
"  padding: -2px;\n"
"}\n"
"QFrame:hover{\n"
"  border: 2px solid #9184e0;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: none;\n"
"	margin: 0;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 10pt;\n"
"	border: none;\n"
"	background-color:"
                        " transparent;\n"
"}\n"
"QLabel:pressed{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QLabel:hover{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QMainWindow {\n"
"	margin: 0px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setMinimumSize(QSize(0, 100))
        self.pushButton_4.setStyleSheet(u"border: none;\n"
"background-color: #1d1d1d;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pin_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u":/icons/pin_white_24dp.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(78, 78))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.password = QFrame(self.centralwidget)
        self.password.setObjectName(u"password")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMaximumSize(QSize(16777215, 41))
        self.password.setFrameShape(QFrame.StyledPanel)
        self.password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.password)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_password = QLineEdit(self.password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	margin: 0;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border: none;\n"
"	margin: 0;\n"
"	background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/visibility_off_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(20, 20))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_2.addWidget(self.btn_visibility)


        self.layout_password.addWidget(self.password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"	margin-left: 0;\n"
"	margin-right: 0;\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #383838;\n"
"  border: 2px solid #9184e0;\n"
"}\n"
"QPushButton:checked{\n"
"  border: 2px solid #9184e0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/rotate_right_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(37, 37))

        self.layout_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton:pressed{\n"
"  background-color: #383838;\n"
"  border: 2px solid #9184e0;\n"
"}\n"
"QPushButton:checked{\n"
"  border: 2px solid #9184e0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(37, 37))

        self.layout_password.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.stronght = QLabel(self.centralwidget)
        self.stronght.setObjectName(u"stronght")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stronght.sizePolicy().hasHeightForWidth())
        self.stronght.setSizePolicy(sizePolicy1)
        self.stronght.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.stronght)

        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy2)
        self.btn_open.setMinimumSize(QSize(36, 30))
        self.btn_open.setMaximumSize(QSize(36, 36))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"  border: 2px solid gray;\n"
"  border: none;\n"
"  font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #242425;\n"
"  border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #242425;\n"
"  border: none;\n"
"  color: black\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/file_open_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open.setIcon(icon5)
        self.btn_open.setIconSize(QSize(24, 24))

        self.layout_info.addWidget(self.btn_open)

        self.entropy = QLabel(self.centralwidget)
        self.entropy.setObjectName(u"entropy")
        sizePolicy1.setHeightForWidth(self.entropy.sizePolicy().hasHeightForWidth())
        self.entropy.setSizePolicy(sizePolicy1)
        self.entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.entropy)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_len = QHBoxLayout()
        self.layout_len.setObjectName(u"layout_len")
        self.slider_len = QSlider(self.centralwidget)
        self.slider_len.setObjectName(u"slider_len")
        self.slider_len.setMinimumSize(QSize(280, 0))
        self.slider_len.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_len.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;    \n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #9184e0;\n"
"    border-radius: 2px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background-color: gray;\n"
"    border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: white;\n"
"    width: 12px;\n"
"    margin: -3px 0; \n"
"    border-radius: 2px;\n"
"}")
        self.slider_len.setMaximum(100)
        self.slider_len.setValue(12)
        self.slider_len.setOrientation(Qt.Horizontal)

        self.layout_len.addWidget(self.slider_len)

        self.spinBox_len = QSpinBox(self.centralwidget)
        self.spinBox_len.setObjectName(u"spinBox_len")
        sizePolicy2.setHeightForWidth(self.spinBox_len.sizePolicy().hasHeightForWidth())
        self.spinBox_len.setSizePolicy(sizePolicy2)
        self.spinBox_len.setMinimumSize(QSize(30, 30))
        self.spinBox_len.setCursor(QCursor(Qt.ArrowCursor))
        self.spinBox_len.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"    background: transparent;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #9184e0;\n"
"}")
        self.spinBox_len.setAlignment(Qt.AlignCenter)
        self.spinBox_len.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_len.setMaximum(100)
        self.spinBox_len.setValue(12)

        self.layout_len.addWidget(self.spinBox_len)


        self.verticalLayout.addLayout(self.layout_len)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setSpacing(15)
        self.layout_characters.setObjectName(u"layout_characters")
        self.layout_characters.setContentsMargins(0, -1, -1, -1)
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_num = QPushButton(self.centralwidget)
        self.btn_num.setObjectName(u"btn_num")
        self.btn_num.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_num.setCheckable(True)
        self.btn_num.setChecked(True)

        self.layout_characters.addWidget(self.btn_num)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_special.setCheckable(True)

        self.layout_characters.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.pushButton_4.setText("")
        self.line_password.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
#if QT_CONFIG(shortcut)
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.stronght.setText("")
        self.btn_open.setText("")
        self.entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_num.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

