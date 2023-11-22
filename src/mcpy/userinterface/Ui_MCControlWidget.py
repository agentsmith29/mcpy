# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MCControlWidget.ui'
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

class Ui_MCControlWindow(object):
    def setupUi(self, MCControlWindow):
        if not MCControlWindow.objectName():
            MCControlWindow.setObjectName(u"MCControlWindow")
        MCControlWindow.resize(510, 532)
        self.gridLayout_2 = QGridLayout(MCControlWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.grd_mcm_members = QGridLayout()
        self.grd_mcm_members.setObjectName(u"grd_mcm_members")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_samples_n = QLabel(MCControlWindow)
        self.lbl_samples_n.setObjectName(u"lbl_samples_n")

        self.gridLayout_3.addWidget(self.lbl_samples_n, 1, 1, 1, 1)

        self.lbl_exp_uncert = QLabel(MCControlWindow)
        self.lbl_exp_uncert.setObjectName(u"lbl_exp_uncert")

        self.gridLayout_3.addWidget(self.lbl_exp_uncert, 7, 1, 1, 1)

        self.label_3 = QLabel(MCControlWindow)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)

        self.txt_std = QLineEdit(MCControlWindow)
        self.txt_std.setObjectName(u"txt_std")

        self.gridLayout_3.addWidget(self.txt_std, 3, 2, 1, 3)

        self.txt_cov = QLineEdit(MCControlWindow)
        self.txt_cov.setObjectName(u"txt_cov")

        self.gridLayout_3.addWidget(self.txt_cov, 5, 2, 1, 1)

        self.text_samples_n = QLineEdit(MCControlWindow)
        self.text_samples_n.setObjectName(u"text_samples_n")

        self.gridLayout_3.addWidget(self.text_samples_n, 1, 2, 1, 3)

        self.lbl_cov_factor = QLabel(MCControlWindow)
        self.lbl_cov_factor.setObjectName(u"lbl_cov_factor")

        self.gridLayout_3.addWidget(self.lbl_cov_factor, 5, 3, 1, 1)

        self.txt_mean = QLineEdit(MCControlWindow)
        self.txt_mean.setObjectName(u"txt_mean")

        self.gridLayout_3.addWidget(self.txt_mean, 2, 2, 1, 3)

        self.lbl_coverage = QLabel(MCControlWindow)
        self.lbl_coverage.setObjectName(u"lbl_coverage")

        self.gridLayout_3.addWidget(self.lbl_coverage, 5, 1, 1, 1)

        self.frame_2 = QFrame(MCControlWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.HLine)
        self.frame_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.frame_2, 8, 1, 1, 4)

        self.txt_unit = QLineEdit(MCControlWindow)
        self.txt_unit.setObjectName(u"txt_unit")

        self.gridLayout_3.addWidget(self.txt_unit, 9, 2, 1, 3)

        self.lbl_std = QLabel(MCControlWindow)
        self.lbl_std.setObjectName(u"lbl_std")

        self.gridLayout_3.addWidget(self.lbl_std, 3, 1, 1, 1)

        self.frame = QFrame(MCControlWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.frame, 4, 1, 1, 4)

        self.txt_cov_factor = QLineEdit(MCControlWindow)
        self.txt_cov_factor.setObjectName(u"txt_cov_factor")

        self.gridLayout_3.addWidget(self.txt_cov_factor, 5, 4, 1, 1)

        self.lbl_unit = QLabel(MCControlWindow)
        self.lbl_unit.setObjectName(u"lbl_unit")

        self.gridLayout_3.addWidget(self.lbl_unit, 9, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(MCControlWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 7, 2, 1, 3)

        self.label = QLabel(MCControlWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 4)


        self.grd_mcm_members.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.grd_mcm_members, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(MCControlWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_plot_area = QWidget()
        self.tab_plot_area.setObjectName(u"tab_plot_area")
        self.grd_plot_area = QGridLayout(self.tab_plot_area)
        self.grd_plot_area.setObjectName(u"grd_plot_area")
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


        self.retranslateUi(MCControlWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MCControlWindow)
    # setupUi

    def retranslateUi(self, MCControlWindow):
        MCControlWindow.setWindowTitle(QCoreApplication.translate("MCControlWindow", u"Form", None))
        self.lbl_samples_n.setText(QCoreApplication.translate("MCControlWindow", u"Number of Samples", None))
        self.lbl_exp_uncert.setText(QCoreApplication.translate("MCControlWindow", u"Expanded Uncertainty", None))
        self.label_3.setText(QCoreApplication.translate("MCControlWindow", u"Mean", None))
        self.lbl_cov_factor.setText(QCoreApplication.translate("MCControlWindow", u"Coverage Factor", None))
        self.lbl_coverage.setText(QCoreApplication.translate("MCControlWindow", u"Coverage [%]", None))
        self.lbl_std.setText(QCoreApplication.translate("MCControlWindow", u"Standard Deviation", None))
        self.lbl_unit.setText(QCoreApplication.translate("MCControlWindow", u"Unit", None))
        self.label.setText(QCoreApplication.translate("MCControlWindow", u"Monte Carlo Samples", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plot_area), QCoreApplication.translate("MCControlWindow", u"Sample Plot", None))
        self.lbl_description.setText(QCoreApplication.translate("MCControlWindow", u"Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_description), QCoreApplication.translate("MCControlWindow", u"Description", None))
    # retranslateUi

