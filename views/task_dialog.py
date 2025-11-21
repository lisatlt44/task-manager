from PySide6.QtWidgets import QDialog, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt, QDateTime
from models.task import TaskStatus
from utils.dialogs import question_oui_non
from views.ui_task_dialog import Ui_TaskDialog
from views.comment_dialog import CommentDialog

class TaskDialog(QDialog):
  """Fenêtre pour créer/modifier une tâche"""

  def __init__(self, controller, parent=None, task=None):
    super().__init__(parent)
    self.ui = Ui_TaskDialog()
    self.ui.setupUi(self)

    self.controller = controller
    self.task = task
    self.is_edit_mode = task is not None

    # Liste pour les commentaires en mode création
    self.pending_comments = []

    self.setup_ui()
    self.connect_signals()

    # Chargement des données si mode édition
    if self.is_edit_mode:
      self.load_task_data()

  def setup_ui(self):
    """Configuration de l'interface"""

    # Titre de la fenêtre
    if self.is_edit_mode:
      self.setWindowTitle("Modifier la tâche")
    else:
      self.setWindowTitle("Nouvelle tâche")

    # Dates par défaut
    now = QDateTime.currentDateTime()
    self.ui.dateTimeEdit_start.setDateTime(now)
    self.ui.dateTimeEdit_end.setDateTime(now)

    # Activation du calendrier
    self.ui.dateTimeEdit_start.setCalendarPopup(True)
    self.ui.dateTimeEdit_end.setCalendarPopup(True)

  def connect_signals(self):
    """Connection des boutons"""

    self.ui.pushButton_add_comment.clicked.connect(self.add_comment)
    self.ui.pushButton_delete_comment.clicked.connect(self.delete_comment)

  def load_task_data(self):
    """Charge les données de la tâche en mode édition"""

    if not self.task:
      return

    # Chargement des informations
    self.ui.lineEdit_title.setText(self.task.title)
    self.ui.textEdit_description.setPlainText(self.task.description)

    # Statut
    status_index = list(TaskStatus).index(self.task.status)
    self.ui.comboBox_status.setCurrentIndex(status_index)

    # Dates
    if self.task.start_date:
      qdt = QDateTime.fromString(
        self.task.start_date.isoformat(),
        Qt.ISODate
      )
      self.ui.dateTimeEdit_start.setDateTime(qdt)

    if self.task.end_date:
      qdt = QDateTime.fromString(
        self.task.end_date.isoformat(),
        Qt.ISODate
      )
      self.ui.dateTimeEdit_end.setDateTime(qdt)

    # Chargement des commentaires
    self.load_comments()

  def load_comments(self):
    """Charge les commentaires de la tâche"""

    self.ui.listWidget_comments.clear()

    if self.is_edit_mode and self.task:
      # Edition => chargement depuis la BDD
      comments = self.controller.get_comments_for_task(self.task.id)
      for comment in comments:
        date_str = comment.created_at.strftime("%d/%m/%Y %H:%M")
        item_text = f"[{date_str}] {comment.content}"
        item = QListWidgetItem(item_text)
        item.setData(Qt.UserRole, comment.id)  # Stocker l'ID du commentaire
        self.ui.listWidget_comments.addItem(item)
    else:
      # Création => affichage des commentaires en attente
      for i, content in enumerate(self.pending_comments):
        item_text = f"[En attente] {content}"
        item = QListWidgetItem(item_text)
        item.setData(Qt.UserRole, i)
        self.ui.listWidget_comments.addItem(item)

  def add_comment(self):
    """Ajoute un commentaire"""

    dialog = CommentDialog(self)

    if dialog.exec():
      content = dialog.get_comment()

      if self.is_edit_mode:
        # Edition => sauvegarde directement en BDD
        success, msg, comment = self.controller.add_comment(self.task.id, content)

        if success:
          self.load_comments()
          QMessageBox.information(self, "Succès", msg)
        else:
          QMessageBox.warning(self, "Erreur", msg)
      else:
        # Création => ajout à la liste temporaire
        self.pending_comments.append(content)
        self.load_comments()
        QMessageBox.information(
          self,
          "Commentaire ajouté",
          "Le commentaire sera ajouté lors de la création de la tâche"
        )

  def delete_comment(self):
    """Supprime un commentaire"""

    current_item = self.ui.listWidget_comments.currentItem()

    if not current_item:
      QMessageBox.warning(self, "Attention", "Veuillez sélectionner un commentaire à supprimer")
      return

    # Confirmation
    if question_oui_non(
      self,
      "Confirmation",
      "Êtes-vous sûr de vouloir supprimer ce commentaire ?"
    ):
      if self.is_edit_mode:
        # Edition => suppression de la BDD
        comment_id = current_item.data(Qt.UserRole)
        success, msg = self.controller.delete_comment(comment_id)

        if success:
          self.load_comments()
        else:
          QMessageBox.warning(self, "Erreur", msg)
      else:
        # Création => retrait de la liste temporaire
        index = current_item.data(Qt.UserRole)
        del self.pending_comments[index]
        self.load_comments()

  def accept(self):
    """Validation et sauvegarde"""

    # Récupération des données
    title = self.ui.lineEdit_title.text().strip()
    description = self.ui.textEdit_description.toPlainText().strip()
    status_index = self.ui.comboBox_status.currentIndex()
    status = list(TaskStatus)[status_index]

    # Conversion des dates
    start_date = self.ui.dateTimeEdit_start.dateTime().toPython()
    end_date = self.ui.dateTimeEdit_end.dateTime().toPython()

    # Création ou modification
    if self.is_edit_mode:
      success, msg = self.controller.update_task(
        self.task.id,
        title,
        description,
        status,
        start_date,
        end_date
      )
    else:
      success, msg, task = self.controller.create_task(
        title,
        description,
        status,
        start_date,
        end_date
      )

      # Si création réussie, ajout des commentaires en attente
      if success and self.pending_comments:
        for content in self.pending_comments:
          self.controller.add_comment(task.id, content)

    if success:
      super().accept()
    else:
      QMessageBox.warning(self, "Erreur de validation", msg)