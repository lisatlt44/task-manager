# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comment_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CommentDialog(object):
    def setupUi(self, CommentDialog):
        if not CommentDialog.objectName():
            CommentDialog.setObjectName(u"CommentDialog")
        CommentDialog.resize(400, 316)
        CommentDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f7;\n"
"}")
        self.verticalLayout = QVBoxLayout(CommentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_comment = QLabel(CommentDialog)
        self.label_comment.setObjectName(u"label_comment")

        self.verticalLayout.addWidget(self.label_comment)

        self.textEdit_comment = QTextEdit(CommentDialog)
        self.textEdit_comment.setObjectName(u"textEdit_comment")
        self.textEdit_comment.setStyleSheet(u"QTextEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d2d2d7;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    min-height: 120px;\n"
"}")

        self.verticalLayout.addWidget(self.textEdit_comment)

        self.label_date = QLabel(CommentDialog)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout.addWidget(self.label_date)

        self.buttonBox = QDialogButtonBox(CommentDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"QDialogButtonBox QPushButton {\n"
"    background-color: #0071e3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    font-size: 13px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:hover {\n"
"    background-color: #0077ed;\n"
"}")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CommentDialog)
        self.buttonBox.accepted.connect(CommentDialog.accept)
        self.buttonBox.rejected.connect(CommentDialog.reject)

        QMetaObject.connectSlotsByName(CommentDialog)
    # setupUi

    def retranslateUi(self, CommentDialog):
        CommentDialog.setWindowTitle(QCoreApplication.translate("CommentDialog", u"Ajouter un commentaire", None))
        self.label_comment.setText(QCoreApplication.translate("CommentDialog", u"Commentaire :", None))
        self.label_date.setText(QCoreApplication.translate("CommentDialog", u"Date : (automatique)", None))
    # retranslateUi

