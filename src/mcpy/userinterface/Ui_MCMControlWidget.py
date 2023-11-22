# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MCMControlWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QTabWidget,
    QWidget)

class Ui_MCMControlWindow(object):
    def setupUi(self, MCMControlWindow):
        if not MCMControlWindow.objectName():
            MCMControlWindow.setObjectName(u"MCMControlWindow")
        MCMControlWindow.resize(510, 532)
        self.gridLayout_2 = QGridLayout(MCMControlWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.grd_mcm_members = QGridLayout()
        self.grd_mcm_members.setObjectName(u"grd_mcm_members")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_samples_n = QLabel(MCMControlWindow)
        self.lbl_samples_n.setObjectName(u"lbl_samples_n")

        self.gridLayout_3.addWidget(self.lbl_samples_n, 1, 1, 1, 1)

        self.label_2 = QLabel(MCMControlWindow)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 7, 1, 1, 1)

        self.label_3 = QLabel(MCMControlWindow)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)

        self.txt_std = QLineEdit(MCMControlWindow)
        self.txt_std.setObjectName(u"txt_std")

        self.gridLayout_3.addWidget(self.txt_std, 3, 2, 1, 3)

        self.lineEdit = QLineEdit(MCMControlWindow)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 5, 2, 1, 1)

        self.text_samples_n = QLineEdit(MCMControlWindow)
        self.text_samples_n.setObjectName(u"text_samples_n")

        self.gridLayout_3.addWidget(self.text_samples_n, 1, 2, 1, 3)

        self.lbl_cov_factor = QLabel(MCMControlWindow)
        self.lbl_cov_factor.setObjectName(u"lbl_cov_factor")

        self.gridLayout_3.addWidget(self.lbl_cov_factor, 5, 3, 1, 1)

        self.txt_mean = QLineEdit(MCMControlWindow)
        self.txt_mean.setObjectName(u"txt_mean")

        self.gridLayout_3.addWidget(self.txt_mean, 2, 2, 1, 3)

        self.lbl_coverage = QLabel(MCMControlWindow)
        self.lbl_coverage.setObjectName(u"lbl_coverage")

        self.gridLayout_3.addWidget(self.lbl_coverage, 5, 1, 1, 1)

        self.frame_2 = QFrame(MCMControlWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.HLine)
        self.frame_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.frame_2, 8, 1, 1, 4)

        self.txt_unit = QLineEdit(MCMControlWindow)
        self.txt_unit.setObjectName(u"txt_unit")

        self.gridLayout_3.addWidget(self.txt_unit, 9, 2, 1, 3)

        self.lbl_std = QLabel(MCMControlWindow)
        self.lbl_std.setObjectName(u"lbl_std")

        self.gridLayout_3.addWidget(self.lbl_std, 3, 1, 1, 1)

        self.frame = QFrame(MCMControlWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.frame, 4, 1, 1, 4)

        self.lineEdit_2 = QLineEdit(MCMControlWindow)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 5, 4, 1, 1)

        self.lbl_unit = QLabel(MCMControlWindow)
        self.lbl_unit.setObjectName(u"lbl_unit")

        self.gridLayout_3.addWidget(self.lbl_unit, 9, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(MCMControlWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 7, 2, 1, 3)

        self.label = QLabel(MCMControlWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 4)


        self.grd_mcm_members.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.grd_mcm_members, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(MCMControlWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_plot_area = QWidget()
        self.tab_plot_area.setObjectName(u"tab_plot_area")
        self.gridLayout_8 = QGridLayout(self.tab_plot_area)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget.addTab(self.tab_plot_area, "")
        self.tab_description = QWidget()
        self.tab_description.setObjectName(u"tab_description")
        self.gridLayout_6 = QGridLayout(self.tab_description)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lbl_description = QLabel(self.tab_description)
        self.lbl_description.setObjectName(u"lbl_description")

        self.gridLayout_5.addWidget(self.lbl_description, 0, 0, 1, 1)

        self.txt_description = QPlainTextEdit(self.tab_description)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setMaximumSize(QSize(16777215, 250))

        self.gridLayout_5.addWidget(self.txt_description, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_description, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.retranslateUi(MCMControlWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MCMControlWindow)
    # setupUi

    def retranslateUi(self, MCMControlWindow):
        MCMControlWindow.setWindowTitle(QCoreApplication.translate("MCMControlWindow", u"Form", None))
        self.lbl_samples_n.setText(QCoreApplication.translate("MCMControlWindow", u"Number of Samples", None))
        self.label_2.setText(QCoreApplication.translate("MCMControlWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MCMControlWindow", u"Mean", None))
        self.lbl_cov_factor.setText(QCoreApplication.translate("MCMControlWindow", u"Coverage Factor", None))
        self.lbl_coverage.setText(QCoreApplication.translate("MCMControlWindow", u"Coverage [%]", None))
        self.lbl_std.setText(QCoreApplication.translate("MCMControlWindow", u"Standard Deviation", None))
        self.lbl_unit.setText(QCoreApplication.translate("MCMControlWindow", u"Unit", None))
        self.label.setText(QCoreApplication.translate("MCMControlWindow", u"Monte Carlo Samples", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plot_area), QCoreApplication.translate("MCMControlWindow", u"Sample Plot", None))
        self.lbl_description.setText(QCoreApplication.translate("MCMControlWindow", u"Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_description), QCoreApplication.translate("MCMControlWindow", u"Description", None))
    # retranslateUi

