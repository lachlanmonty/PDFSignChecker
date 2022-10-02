# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'psc_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_PSC_GUI(object):
    def setupUi(self, PSC_GUI):
        if not PSC_GUI.objectName():
            PSC_GUI.setObjectName(u"PSC_GUI")
        PSC_GUI.resize(1080, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSC_GUI.sizePolicy().hasHeightForWidth())
        PSC_GUI.setSizePolicy(sizePolicy)
        PSC_GUI.setMaximumSize(QSize(1080, 600))
        self.centralwidget = QWidget(PSC_GUI)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 90, 241, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.step_1 = QLabel(self.verticalLayoutWidget)
        self.step_1.setObjectName(u"step_1")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        self.step_1.setFont(font)

        self.verticalLayout.addWidget(self.step_1)

        self.open_file_button = QPushButton(self.verticalLayoutWidget)
        self.open_file_button.setObjectName(u"open_file_button")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.open_file_button.setFont(font1)

        self.verticalLayout.addWidget(self.open_file_button)

        self.file_confirm = QLabel(self.verticalLayoutWidget)
        self.file_confirm.setObjectName(u"file_confirm")
        self.file_confirm.setFont(font1)

        self.verticalLayout.addWidget(self.file_confirm)

        self.step_2 = QLabel(self.verticalLayoutWidget)
        self.step_2.setObjectName(u"step_2")
        self.step_2.setFont(font)

        self.verticalLayout.addWidget(self.step_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.run_button = QPushButton(self.verticalLayoutWidget)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.run_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.step_3 = QLabel(self.verticalLayoutWidget)
        self.step_3.setObjectName(u"step_3")
        self.step_3.setFont(font)

        self.verticalLayout.addWidget(self.step_3)

        self.save_button = QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setFont(font1)

        self.verticalLayout.addWidget(self.save_button)

        self.step_4 = QLabel(self.verticalLayoutWidget)
        self.step_4.setObjectName(u"step_4")
        self.step_4.setFont(font)

        self.verticalLayout.addWidget(self.step_4)

        self.step_5 = QLabel(self.verticalLayoutWidget)
        self.step_5.setObjectName(u"step_5")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setUnderline(False)
        self.step_5.setFont(font2)
        self.step_5.setAcceptDrops(False)
        self.step_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.step_5)

        self.save_who_button = QPushButton(self.verticalLayoutWidget)
        self.save_who_button.setObjectName(u"save_who_button")
        self.save_who_button.setFont(font1)

        self.verticalLayout.addWidget(self.save_who_button)

        self.pandas_table = QTableView(self.centralwidget)
        self.pandas_table.setObjectName(u"pandas_table")
        self.pandas_table.setGeometry(QRect(260, 90, 811, 501))
        self.pandas_table.setSortingEnabled(True)
        self.pandas_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.pandas_table.verticalHeader().setProperty("showSortIndicator", False)
        self.tile = QLabel(self.centralwidget)
        self.tile.setObjectName(u"tile")
        self.tile.setGeometry(QRect(10, 0, 402, 51))
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(False)
        font3.setItalic(False)
        self.tile.setFont(font3)
        self.tile.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.description = QLabel(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(10, 47, 402, 41))
        self.description.setFont(font1)
        PSC_GUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(PSC_GUI)

        QMetaObject.connectSlotsByName(PSC_GUI)
    # setupUi

    def retranslateUi(self, PSC_GUI):
        PSC_GUI.setWindowTitle(QCoreApplication.translate("PSC_GUI", u"PDF Signature Checker", None))
        self.step_1.setText(QCoreApplication.translate("PSC_GUI", u"Step 1: Select pdfs", None))
        self.open_file_button.setText(QCoreApplication.translate("PSC_GUI", u"Open File/s", None))
        self.file_confirm.setText("")
        self.step_2.setText(QCoreApplication.translate("PSC_GUI", u"Step 2: Check if signed", None))
        self.run_button.setText(QCoreApplication.translate("PSC_GUI", u"Run", None))
        self.step_3.setText(QCoreApplication.translate("PSC_GUI", u"Optional: Save output to excel", None))
        self.save_button.setText(QCoreApplication.translate("PSC_GUI", u"Save Excel File", None))
        self.step_4.setText(QCoreApplication.translate("PSC_GUI", u"Optional: Who hasn't signed?", None))
        self.step_5.setText(QCoreApplication.translate("PSC_GUI", u"Save a list of everyone who hasnt signed the pdfs.", None))
        self.save_who_button.setText(QCoreApplication.translate("PSC_GUI", u"Save Excel File", None))
        self.tile.setText(QCoreApplication.translate("PSC_GUI", u"PDF Signature Checker", None))
        self.description.setText(QCoreApplication.translate("PSC_GUI", u"Simple GUI to check the status of signatures in pdf files.", None))
    # retranslateUi

