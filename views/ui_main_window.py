# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_filter = QHBoxLayout()
        self.horizontalLayout_filter.setObjectName(u"horizontalLayout_filter")
        self.label_filter = QLabel(self.centralwidget)
        self.label_filter.setObjectName(u"label_filter")

        self.horizontalLayout_filter.addWidget(self.label_filter)

        self.comboBox_filter = QComboBox(self.centralwidget)
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.setObjectName(u"comboBox_filter")
        self.comboBox_filter.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #0071e3;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    selection-background-color: #0071e3;\n"
"    selection-color: white;\n"
"}")

        self.horizontalLayout_filter.addWidget(self.comboBox_filter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filter.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_filter)

        self.tableWidget_tasks = QTableWidget(self.centralwidget)
        if (self.tableWidget_tasks.columnCount() < 4):
            self.tableWidget_tasks.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tasks.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tasks.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tasks.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tasks.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_tasks.setObjectName(u"tableWidget_tasks")
        self.tableWidget_tasks.setStyleSheet(u"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 8px;\n"
"    gridline-color: #e5e5ea;\n"
"    selection-background-color: #0071e3;\n"
"    selection-color: white;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 10px 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f5f5f7;\n"
"    padding: 10px 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #d2d2d7;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}")
        self.tableWidget_tasks.setAlternatingRowColors(True)
        self.tableWidget_tasks.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_tasks.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_tasks.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tasks.verticalHeader().setDefaultSectionSize(45)

        self.verticalLayout.addWidget(self.tableWidget_tasks)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setStyleSheet(u"QPushButton {\n"
"    background-color: #0071e3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0077ed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #006edb;\n"
"}")

        self.horizontalLayout_buttons.addWidget(self.pushButton_add)

        self.pushButton_edit = QPushButton(self.centralwidget)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setStyleSheet(u"QPushButton {\n"
"    background-color: #0071e3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0077ed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #006edb;\n"
"}")

        self.horizontalLayout_buttons.addWidget(self.pushButton_edit)

        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"    background-color: #0071e3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0077ed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #006edb;\n"
"}")

        self.horizontalLayout_buttons.addWidget(self.pushButton_close)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff3b30;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ff453a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e6342a;\n"
"}")

        self.horizontalLayout_buttons.addWidget(self.pushButton_delete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestionnaire de T\u00e2ches", None))
        self.label_filter.setText(QCoreApplication.translate("MainWindow", u"Filtrer par \u00e9tat :", None))
        self.comboBox_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"Tous", None))
        self.comboBox_filter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c0 faire", None))
        self.comboBox_filter.setItemText(2, QCoreApplication.translate("MainWindow", u"En cours", None))
        self.comboBox_filter.setItemText(3, QCoreApplication.translate("MainWindow", u"R\u00e9alis\u00e9", None))
        self.comboBox_filter.setItemText(4, QCoreApplication.translate("MainWindow", u"Abandonn\u00e9", None))
        self.comboBox_filter.setItemText(5, QCoreApplication.translate("MainWindow", u"En attente", None))

        ___qtablewidgetitem = self.tableWidget_tasks.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Titre", None));
        ___qtablewidgetitem1 = self.tableWidget_tasks.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u00c9tat", None));
        ___qtablewidgetitem2 = self.tableWidget_tasks.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date d\u00e9but", None));
        ___qtablewidgetitem3 = self.tableWidget_tasks.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date fin", None));
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"Cl\u00f4turer", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
    # retranslateUi

