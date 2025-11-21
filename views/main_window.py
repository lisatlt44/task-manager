from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from models.task import TaskStatus
from controllers.task_controller import TaskController
from utils.dialogs import question_oui_non
from views.ui_main_window import Ui_MainWindow
from views.task_dialog import TaskDialog

class MainWindow(QMainWindow):
  """Fenêtre principale de l'application"""

  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.controller = TaskController()

    self.setup_ui()
    self.connect_signals()
    self.load_tasks()

  def setup_ui(self):
    """Configuration de l'interface au démarrage"""

    # Taille des colonnes
    self.ui.tableWidget_tasks.setColumnWidth(0, 300)
    self.ui.tableWidget_tasks.setColumnWidth(1, 150)
    self.ui.tableWidget_tasks.setColumnWidth(2, 150)
    self.ui.tableWidget_tasks.setColumnWidth(3, 150)

    # Activation du tri sur les colonnes
    self.ui.tableWidget_tasks.setSortingEnabled(True)

  def connect_signals(self):
    """Connections des boutons aux fonctions"""

    self.ui.pushButton_add.clicked.connect(self.add_task)
    self.ui.pushButton_edit.clicked.connect(self.edit_task)
    self.ui.pushButton_delete.clicked.connect(self.delete_task)
    self.ui.pushButton_close.clicked.connect(self.close_task)
    self.ui.comboBox_filter.currentIndexChanged.connect(self.load_tasks)
    self.ui.tableWidget_tasks.doubleClicked.connect(self.edit_task)

  def load_tasks(self):
    """Charge et affiche les tâches selon le filtre"""

    # Désactivation du tri pendant le chargement
    self.ui.tableWidget_tasks.setSortingEnabled(False)

    # Récupération du filtre
    filter_text = self.ui.comboBox_filter.currentText()

    if filter_text == "Tous":
      tasks = self.controller.get_all_tasks()
    else:
      # Trouver le statut correspondant
      status = None
      for s in TaskStatus:
        if s.value == filter_text:
          status = s
          break

      tasks = self.controller.get_tasks_by_status(status)

    # Remplissage du tableau
    self.ui.tableWidget_tasks.setRowCount(len(tasks))

    for row, task in enumerate(tasks):
      # Titre
      item_title = QTableWidgetItem(task.title)
      item_title.setData(Qt.UserRole, task.id)
      self.ui.tableWidget_tasks.setItem(row, 0, item_title)

      # État
      item_status = QTableWidgetItem(task.status.value)
      self.ui.tableWidget_tasks.setItem(row, 1, item_status)

      # Date début
      if task.start_date:
        start_date_str = task.start_date.strftime("%d/%m/%Y %H:%M")
        item_start = QTableWidgetItem(start_date_str)
        item_start.setData(Qt.UserRole + 1, task.start_date.timestamp())
      else:
        item_start = QTableWidgetItem("-")
        item_start.setData(Qt.UserRole + 1, 0)
      self.ui.tableWidget_tasks.setItem(row, 2, item_start)

      # Date fin
      if task.end_date:
        end_date_str = task.end_date.strftime("%d/%m/%Y %H:%M")
        item_end = QTableWidgetItem(end_date_str)
        item_end.setData(Qt.UserRole + 1, task.end_date.timestamp())
      else:
        item_end = QTableWidgetItem("-")
        item_end.setData(Qt.UserRole + 1, 0)
      self.ui.tableWidget_tasks.setItem(row, 3, item_end)

    # Réactivation du tri
    self.ui.tableWidget_tasks.setSortingEnabled(True)

    # Affichage du nombre de tâches
    self.statusBar().showMessage(f"{len(tasks)} tâche(s)")

  def add_task(self):
    """Ouvre la fenêtre pour ajouter une tâche"""

    dialog = TaskDialog(self.controller, self)
    if dialog.exec():
      self.load_tasks()
      QMessageBox.information(self, "Succès", "Tâche créée avec succès")

  def edit_task(self):
    """Ouvre la fenêtre pour modifier une tâche"""

    current_row = self.ui.tableWidget_tasks.currentRow()

    if current_row < 0:
      QMessageBox.warning(self, "Attention", "Veuillez sélectionner une tâche à modifier")
      return

    # Récupération de l'ID de la tâche
    item = self.ui.tableWidget_tasks.item(current_row, 0)
    task_id = item.data(Qt.UserRole)

    # Récupération de la tâche complète
    task = self.controller.get_task_by_id(task_id)

    if task:
      dialog = TaskDialog(self.controller, self, task)
      if dialog.exec():
        self.load_tasks()
        QMessageBox.information(self, "Succès", "Tâche mise à jour avec succès")

  def delete_task(self):
    """Supprime la tâche sélectionnée"""

    current_row = self.ui.tableWidget_tasks.currentRow()

    if current_row < 0:
      QMessageBox.warning(self, "Attention", "Veuillez sélectionner une tâche à supprimer")
      return

    # Demande confirmation
    if question_oui_non(
      self,
      "Confirmation",
      "Êtes-vous sûr de vouloir supprimer cette tâche ?\nTous les commentaires seront également supprimés."
    ):
      item = self.ui.tableWidget_tasks.item(current_row, 0)
      task_id = item.data(Qt.UserRole)

      success, msg = self.controller.delete_task(task_id)

      if success:
        self.load_tasks()
        QMessageBox.information(self, "Succès", msg)
      else:
        QMessageBox.warning(self, "Erreur", msg)

  def close_task(self):
    """Clôture la tâche sélectionnée"""

    current_row = self.ui.tableWidget_tasks.currentRow()

    if current_row < 0:
      QMessageBox.warning(self, "Attention", "Veuillez sélectionner une tâche à clôturer")
      return

    # Demande confirmation
    if question_oui_non(
      self,
      "Confirmation",
      "Êtes-vous sûr de vouloir clôturer cette tâche ?"
    ):
      item = self.ui.tableWidget_tasks.item(current_row, 0)
      task_id = item.data(Qt.UserRole)

      success, msg = self.controller.close_task(task_id)

      if success:
        self.load_tasks()
        QMessageBox.information(self, "Succès", msg)
      else:
        QMessageBox.warning(self, "Erreur", msg)