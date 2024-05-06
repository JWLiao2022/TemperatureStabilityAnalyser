# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(1366, 768))
        Widget.setMaximumSize(QSize(1366, 768))
        self.graphicsViewPlot = PlotWidget(Widget)
        self.graphicsViewPlot.setObjectName(u"graphicsViewPlot")
        self.graphicsViewPlot.setGeometry(QRect(30, 180, 1041, 571))
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 0, 641, 161))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.pushButtonLocateStabilityResult = QPushButton(self.groupBox)
        self.pushButtonLocateStabilityResult.setObjectName(u"pushButtonLocateStabilityResult")
        self.pushButtonLocateStabilityResult.setGeometry(QRect(540, 30, 80, 31))
        self.lineEditStabilityResultFilePath = QLineEdit(self.groupBox)
        self.lineEditStabilityResultFilePath.setObjectName(u"lineEditStabilityResultFilePath")
        self.lineEditStabilityResultFilePath.setGeometry(QRect(20, 30, 501, 31))

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.pushButtonLocateTemperatureVariation = QPushButton(self.groupBox_2)
        self.pushButtonLocateTemperatureVariation.setObjectName(u"pushButtonLocateTemperatureVariation")
        self.pushButtonLocateTemperatureVariation.setGeometry(QRect(540, 30, 80, 31))
        self.lineEditTemperatureVariationsFilePath = QLineEdit(self.groupBox_2)
        self.lineEditTemperatureVariationsFilePath.setObjectName(u"lineEditTemperatureVariationsFilePath")
        self.lineEditTemperatureVariationsFilePath.setGeometry(QRect(20, 30, 501, 31))

        self.verticalLayout.addWidget(self.groupBox_2)

        self.widget1 = QWidget(Widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(700, 10, 371, 151))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonPlot = QPushButton(self.widget1)
        self.pushButtonPlot.setObjectName(u"pushButtonPlot")
        self.pushButtonPlot.setMinimumSize(QSize(20, 80))

        self.horizontalLayout.addWidget(self.pushButtonPlot)

        self.pushButtonSavePlots = QPushButton(self.widget1)
        self.pushButtonSavePlots.setObjectName(u"pushButtonSavePlots")
        self.pushButtonSavePlots.setMinimumSize(QSize(0, 80))

        self.horizontalLayout.addWidget(self.pushButtonSavePlots)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Temperature stability analyser", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Stability results from ML3", None))
        self.pushButtonLocateStabilityResult.setText(QCoreApplication.translate("Widget", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Temperature variations from a seperate thermal couple", None))
        self.pushButtonLocateTemperatureVariation.setText(QCoreApplication.translate("Widget", u"...", None))
        self.pushButtonPlot.setText(QCoreApplication.translate("Widget", u"Plot!", None))
        self.pushButtonSavePlots.setText(QCoreApplication.translate("Widget", u"Save the plots!", None))
    # retranslateUi

