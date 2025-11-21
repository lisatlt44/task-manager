from datetime import datetime
from models.database import Database
from models.task import Task, TaskStatus
from models.comment import Comment
from utils.validators import TaskValidator, CommentValidator

class TaskController:
  """Le contrôleur qui gère toute la logique métier"""

  def __init__(self, db_path="data/tasks.db"):
    self.db = Database(db_path)

  def create_task(self, title, description="", status=TaskStatus.TODO, start_date=None, end_date=None):
    """Crée une nouvelle tâche avec validation"""

    # Validation
    valid, error = TaskValidator.validate_title(title)
    if not valid:
      return False, error, None

    valid, error = TaskValidator.validate_description(description)
    if not valid:
      return False, error, None

    valid, error = TaskValidator.validate_dates(start_date, end_date)
    if not valid:
      return False, error, None

    # Création de la tâche
    task = Task(
      title=title.strip(),
      description=description.strip(),
      status=status,
      start_date=start_date,
      end_date=end_date
    )

    # Sauvegarde en BDD
    if self.db.add_task(task):
      return True, "Tâche créée avec succès", task
    else:
      return False, "Erreur lors de la sauvegarde", None

  def update_task(self, task_id, title, description, status, start_date, end_date):
    """Met à jour une tâche existante"""

    # Validation
    valid, error = TaskValidator.validate_title(title)
    if not valid:
      return False, error

    valid, error = TaskValidator.validate_description(description)
    if not valid:
      return False, error

    valid, error = TaskValidator.validate_dates(start_date, end_date)
    if not valid:
      return False, error

    # Récupération de la tâche
    tasks = self.db.get_all_tasks()
    task = None
    for t in tasks:
      if t.id == task_id:
        task = t
        break

    if not task:
      return False, "Tâche non trouvée"

    # Mise à jour
    task.title = title.strip()
    task.description = description.strip()
    task.status = status
    task.start_date = start_date
    task.end_date = end_date

    if self.db.update_task(task):
      return True, "Tâche mise à jour avec succès"
    else:
      return False, "Erreur lors de la mise à jour"

  def delete_task(self, task_id):
    """Supprime une tâche"""

    if self.db.delete_task(task_id):
      return True, "Tâche supprimée avec succès"
    else:
      return False, "Erreur lors de la suppression"

  def close_task(self, task_id):
    """Clôture une tâche"""

    # Récupération de la tâche
    tasks = self.db.get_all_tasks()
    task = None
    for t in tasks:
      if t.id == task_id:
        task = t
        break

    if not task:
      return False, "Tâche non trouvée"

    if task.status == TaskStatus.DONE:
      return False, "La tâche est déjà clôturée"

    # Clôture
    task.status = TaskStatus.DONE
    task.end_date = datetime.now()

    if self.db.update_task(task):
      return True, "Tâche clôturée avec succès"
    else:
      return False, "Erreur lors de la clôture"

  def get_all_tasks(self):
    """Récupère toutes les tâches"""

    return self.db.get_all_tasks()

  def get_tasks_by_status(self, status=None):
    """Filtre les tâches par statut"""

    all_tasks = self.db.get_all_tasks()

    # Pas de filtre = tout
    if status is None:
      return all_tasks

    # Filtrage
    filtered = []
    for task in all_tasks:
      if task.status == status:
        filtered.append(task)

    return filtered
  
  def get_task_by_id(self, task_id):
    """Récupère une tâche par son ID"""

    tasks = self.db.get_all_tasks()

    for task in tasks:
      if task.id == task_id:
        return task

    return None

  def add_comment(self, task_id, content):
    """Ajoute un commentaire à une tâche"""

    # Validation
    valid, error = CommentValidator.validate_content(content)
    if not valid:
      return False, error, None

    # Vérification si tâche existe
    task = self.get_task_by_id(task_id)
    if not task:
      return False, "Tâche non trouvée", None

    # Création du commentaire
    comment = Comment(
      content=content.strip(),
      task_id=task_id
    )

    if self.db.add_comment(comment):
      return True, "Commentaire ajouté avec succès", comment
    else:
      return False, "Erreur lors de l'ajout du commentaire", None

  def delete_comment(self, comment_id):
    """Supprime un commentaire"""

    if self.db.delete_comment(comment_id):
      return True, "Commentaire supprimé avec succès"
    else:
      return False, "Erreur lors de la suppression du commentaire"

  def get_comments_for_task(self, task_id):
    """Récupère tous les commentaires d'une tâche"""

    return self.db.get_comments_by_task(task_id)