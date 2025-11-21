from PySide6.QtWidgets import QDialog, QMessageBox
from datetime import datetime
from views.ui_comment_dialog import Ui_CommentDialog

class CommentDialog(QDialog):
  """Fenêtre pour ajouter un commentaire"""

  def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_CommentDialog()
    self.ui.setupUi(self)

    # Afficher la date actuelle
    date_str = datetime.now().strftime('%d/%m/%Y %H:%M')
    self.ui.label_date.setText(f"Date: {date_str}")

    self.comment_content = ""

  def accept(self):
    """Validation avant fermeture"""

    content = self.ui.textEdit_comment.toPlainText().strip()

    if not content:
      QMessageBox.warning(self, "Erreur", "Le commentaire ne peut pas être vide")
      return

    self.comment_content = content
    super().accept()

  def get_comment(self) -> str:
    """Retourne le contenu du commentaire"""

    return self.comment_content