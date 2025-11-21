from datetime import datetime
import uuid

class Comment:
  """Un commentaire lié à une tâche"""

  def __init__(self, content, task_id, comment_id=None, created_at=None):
    self.id = comment_id if comment_id else str(uuid.uuid4())
    self.content = content
    self.task_id = task_id
    self.created_at = created_at if created_at else datetime.now()
  
  def to_dict(self):
    """Pour la base de données"""
    return {
      'id': self.id,
      'task_id': self.task_id,
      'content': self.content,
      'created_at': self.created_at.isoformat()
    }