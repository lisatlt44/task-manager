# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_TaskDialog(object):
    def setupUi(self, TaskDialog):
        if not TaskDialog.objectName():
            TaskDialog.setObjectName(u"TaskDialog")
        TaskDialog.resize(600, 555)
        TaskDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f7;\n"
"}")
        self.verticalLayout = QVBoxLayout(TaskDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_task = QGroupBox(TaskDialog)
        self.groupBox_task.setObjectName(u"groupBox_task")
        self.formLayout = QFormLayout(self.groupBox_task)
        self.formLayout.setObjectName(u"formLayout")
        self.label_title = QLabel(self.groupBox_task)
        self.label_title.setObjectName(u"label_title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_title)

        self.lineEdit_title = QLineEdit(self.groupBox_task)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0071e3;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_title)

        self.label_description = QLabel(self.groupBox_task)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f7;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_description)

        self.textEdit_description = QTextEdit(self.groupBox_task)
        self.textEdit_description.setObjectName(u"textEdit_description")
        self.textEdit_description.setMaximumSize(QSize(16777215, 80))
        self.textEdit_description.setStyleSheet(u"QTextEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #0071e3;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.textEdit_description)

        self.label_status = QLabel(self.groupBox_task)
        self.label_status.setObjectName(u"label_status")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_status)

        self.comboBox_status = QComboBox(self.groupBox_task)
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.setObjectName(u"comboBox_status")
        self.comboBox_status.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_status)

        self.label_start_date = QLabel(self.groupBox_task)
        self.label_start_date.setObjectName(u"label_start_date")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_start_date)

        self.dateTimeEdit_start = QDateTimeEdit(self.groupBox_task)
        self.dateTimeEdit_start.setObjectName(u"dateTimeEdit_start")
        self.dateTimeEdit_start.setStyleSheet(u"QDateTimeEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QDateTimeEdit:focus {\n"
"    border: 2px solid #0071e3;\n"
"}")
        self.dateTimeEdit_start.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateTimeEdit_start)

        self.label_end_date = QLabel(self.groupBox_task)
        self.label_end_date.setObjectName(u"label_end_date")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_end_date)

        self.dateTimeEdit_end = QDateTimeEdit(self.groupBox_task)
        self.dateTimeEdit_end.setObjectName(u"dateTimeEdit_end")
        self.dateTimeEdit_end.setStyleSheet(u"QDateTimeEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QDateTimeEdit:focus {\n"
"    border: 2px solid #0071e3;\n"
"}")
        self.dateTimeEdit_end.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dateTimeEdit_end)


        self.verticalLayout.addWidget(self.groupBox_task)

        self.groupBox_comments = QGroupBox(TaskDialog)
        self.groupBox_comments.setObjectName(u"groupBox_comments")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_comments)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget_comments = QListWidget(self.groupBox_comments)
        self.listWidget_comments.setObjectName(u"listWidget_comments")
        self.listWidget_comments.setStyleSheet(u"QListWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px;\n"
"    border-radius: 4px;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0071e3;\n"
"    color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.listWidget_comments)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_delete_comment = QPushButton(self.groupBox_comments)
        self.pushButton_delete_comment.setObjectName(u"pushButton_delete_comment")
        self.pushButton_delete_comment.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff3b30;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_delete_comment)

        self.pushButton_add_comment = QPushButton(self.groupBox_comments)
        self.pushButton_add_comment.setObjectName(u"pushButton_add_comment")
        self.pushButton_add_comment.setStyleSheet(u"QPushButton {\n"
"    background-color: #0071e3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_add_comment)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_comments)

        self.buttonBox = QDialogButtonBox(TaskDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TaskDialog)
        self.buttonBox.accepted.connect(TaskDialog.accept)
        self.buttonBox.rejected.connect(TaskDialog.reject)

        QMetaObject.connectSlotsByName(TaskDialog)
    # setupUi

    def retranslateUi(self, TaskDialog):
        TaskDialog.setWindowTitle(QCoreApplication.translate("TaskDialog", u"D\u00e9tails de la t\u00e2che", None))
        self.groupBox_task.setTitle(QCoreApplication.translate("TaskDialog", u"Informations de la t\u00e2che", None))
        self.label_title.setText(QCoreApplication.translate("TaskDialog", u"Titre :", None))
        self.label_description.setText(QCoreApplication.translate("TaskDialog", u"Description :", None))
        self.label_status.setText(QCoreApplication.translate("TaskDialog", u"\u00c9tat :", None))
        self.comboBox_status.setItemText(0, QCoreApplication.translate("TaskDialog", u"\u00c0 faire", None))
        self.comboBox_status.setItemText(1, QCoreApplication.translate("TaskDialog", u"En cours", None))
        self.comboBox_status.setItemText(2, QCoreApplication.translate("TaskDialog", u"R\u00e9alis\u00e9", None))
        self.comboBox_status.setItemText(3, QCoreApplication.translate("TaskDialog", u"Abandonn\u00e9", None))
        self.comboBox_status.setItemText(4, QCoreApplication.translate("TaskDialog", u"En attente", None))

        self.label_start_date.setText(QCoreApplication.translate("TaskDialog", u"Date d\u00e9but :", None))
        self.label_end_date.setText(QCoreApplication.translate("TaskDialog", u"Date fin :", None))
        self.groupBox_comments.setTitle(QCoreApplication.translate("TaskDialog", u"Commentaires", None))
        self.pushButton_delete_comment.setText(QCoreApplication.translate("TaskDialog", u"Supprimer", None))
        self.pushButton_add_comment.setText(QCoreApplication.translate("TaskDialog", u"Ajouter un commentaire", None))
    # retranslateUi

