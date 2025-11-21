from PySide6.QtWidgets import QMessageBox

def question_oui_non(parent, title, message):
  """Affiche une confirmation Oui/Non"""

  msg_box = QMessageBox(parent)
  msg_box.setWindowTitle(title)
  msg_box.setText(message)
  msg_box.setIcon(QMessageBox.Question)

  # Oui en surbrillance
  btn_non = msg_box.addButton("Non", QMessageBox.NoRole)
  btn_oui = msg_box.addButton("Oui", QMessageBox.YesRole)
  msg_box.setDefaultButton(btn_oui)

  msg_box.exec()

  return msg_box.clickedButton() == btn_oui