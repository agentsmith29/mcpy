# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UncertaintyControlWidget.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_UncertaintyControlWidget(object):
    def setupUi(self, UncertaintyControlWidget):
        if not UncertaintyControlWidget.objectName():
            UncertaintyControlWidget.setObjectName(u"UncertaintyControlWidget")
        UncertaintyControlWidget.resize(427, 478)
        self.gridLayout = QGridLayout(UncertaintyControlWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(UncertaintyControlWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(UncertaintyControlWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(16777215, 350))
        self.plot_area = QWidget()
        self.plot_area.setObjectName(u"plot_area")
        self.grd_plot_area = QGridLayout(self.plot_area)
        self.grd_plot_area.setObjectName(u"grd_plot_area")
        self.tabWidget.addTab(self.plot_area, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.text_description = QPlainTextEdit(self.tab)
        self.text_description.setObjectName(u"text_description")
        sizePolicy.setHeightForWidth(self.text_description.sizePolicy().hasHeightForWidth())
        self.text_description.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.text_description, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.text_unit = QLineEdit(self.tab)
        self.text_unit.setObjectName(u"text_unit")

        self.gridLayout_5.addWidget(self.text_unit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)

        self.txt_definition = QLineEdit(self.tab)
        self.txt_definition.setObjectName(u"txt_definition")

        self.gridLayout_5.addWidget(self.txt_definition, 1, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 6, 0, 1, 1)

        self.verticalFrame_2 = QFrame(UncertaintyControlWidget)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.grd_unc_info = QVBoxLayout(self.verticalFrame_2)
        self.grd_unc_info.setObjectName(u"grd_unc_info")

        self.gridLayout.addWidget(self.verticalFrame_2, 5, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.cb_type = QComboBox(UncertaintyControlWidget)
        self.cb_type.setObjectName(u"cb_type")

        self.gridLayout_7.addWidget(self.cb_type, 2, 1, 1, 1)

        self.label_3 = QLabel(UncertaintyControlWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(UncertaintyControlWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.label_2, 2, 0, 1, 1)

        self.cb_distribution = QComboBox(UncertaintyControlWidget)
        self.cb_distribution.setObjectName(u"cb_distribution")
        self.cb_distribution.setEditable(False)

        self.gridLayout_7.addWidget(self.cb_distribution, 3, 1, 1, 1)

        self.label = QLabel(UncertaintyControlWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 22))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)

        self.btn_open_mcm = QPushButton(UncertaintyControlWidget)
        self.btn_open_mcm.setObjectName(u"btn_open_mcm")

        self.gridLayout_7.addWidget(self.btn_open_mcm, 4, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.retranslateUi(UncertaintyControlWidget)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(UncertaintyControlWidget)
    # setupUi

    def retranslateUi(self, UncertaintyControlWidget):
        UncertaintyControlWidget.setWindowTitle(QCoreApplication.translate("UncertaintyControlWidget", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot_area), QCoreApplication.translate("UncertaintyControlWidget", u"PDF", None))
        self.label_4.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Unit", None))
        self.label_5.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Definition", None))
        self.label_7.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("UncertaintyControlWidget", u"Details", None))
        self.label_6.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Expanded Uncertainty", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("UncertaintyControlWidget", u"GUM 6.2.1 [p. 23]\n"
"The expanded uncertainty U is obtained by multiplying the combined standard uncertainty uc(y) by a coverage factor k.\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("UncertaintyControlWidget", u"Details", None))
        self.label_3.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Uncertainty Distribution", None))
        self.label_2.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Type", None))
        self.label.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Uncertainty", None))
        self.btn_open_mcm.setText(QCoreApplication.translate("UncertaintyControlWidget", u"Open Monte Carlo Samples", None))
    # retranslateUi

