from enum import Enum
import uuid

class TaskStatus(Enum):
  """Les 5 états d'une tâche"""
  TODO = "À faire"
  IN_PROGRESS = "En cours"
  DONE = "Réalisé"
  ABANDONED = "Abandonné"
  WAITING = "En attente"

class Task:
  """Une tâche"""

  def __init__(self, title, status, task_id=None, description="", start_date=None, end_date=None, comments=None):
    self.id = task_id if task_id else str(uuid.uuid4())
    self.title = title
    self.description = description
    self.start_date = start_date
    self.end_date = end_date
    self.status = status
    self.comments = comments if comments else []

  def to_dict(self):
    """Pour la base de données"""
    return {
      'id': self.id,
      'title': self.title,
      'description': self.description,
      'start_date': self.start_date.isoformat() if self.start_date else None,
      'end_date': self.end_date.isoformat() if self.end_date else None,
      'status': self.status.value
    }