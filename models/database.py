import sqlite3
from datetime import datetime
from models.task import Task, TaskStatus
from models.comment import Comment

class Database:
  """Gère la base de données SQLite"""

  def __init__(self, db_path="data/tasks.db"):
    self.db_path = db_path
    self.init_database()

  def init_database(self):
    """Crée les tables si elles n'existent pas"""

    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()

    # Table pour les tâches
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        start_date TEXT,
        end_date TEXT,
        status TEXT NOT NULL
      )
    ''')

    # Table pour les commentaires
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS comments (
        id TEXT PRIMARY KEY,
        task_id TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL,
        FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE
      )
    ''')

    conn.commit()
    conn.close()

  def add_task(self, task):
    """Ajoute une tâche dans la base"""

    try:
      conn = sqlite3.connect(self.db_path)
      cursor = conn.cursor()
      cursor.execute('''
        INSERT INTO tasks (id, title, description, start_date, end_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
      ''', (
        task.id,
        task.title,
        task.description,
        task.start_date.isoformat() if task.start_date else None,
        task.end_date.isoformat() if task.end_date else None,
        task.status.value
      ))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      print(f"Erreur ajout tâche: {e}")
      return False

  def get_all_tasks(self):
    """Récupère toutes les tâches"""

    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
      task = Task(
        task_id=row[0],
        title=row[1],
        description=row[2],
        start_date=datetime.fromisoformat(row[3]) if row[3] else None,
        end_date=datetime.fromisoformat(row[4]) if row[4] else None,
        status=TaskStatus(row[5])
      )
      # Charger les commentaires de chaque tâche
      task.comments = self.get_comments_by_task(task.id)
      tasks.append(task)

    return tasks

  def update_task(self, task):
    """Met à jour une tâche existante"""

    try:
      conn = sqlite3.connect(self.db_path)
      cursor = conn.cursor()
      cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, start_date = ?, end_date = ?, status = ?
        WHERE id = ?
      ''', (
        task.title,
        task.description,
        task.start_date.isoformat() if task.start_date else None,
        task.end_date.isoformat() if task.end_date else None,
        task.status.value,
        task.id
      ))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      print(f"Erreur mise à jour: {e}")
      return False

  def delete_task(self, task_id):
    """Supprime une tâche et tous ses commentaires"""

    try:
      conn = sqlite3.connect(self.db_path)
      cursor = conn.cursor()
      # Suppression des commentaires d'abord
      cursor.execute('DELETE FROM comments WHERE task_id = ?', (task_id,))
      # Puis suppression de la tâche
      cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      print(f"Erreur suppression: {e}")
      return False

  def add_comment(self, comment):
    """Ajoute un commentaire à une tâche"""

    try:
      conn = sqlite3.connect(self.db_path)
      cursor = conn.cursor()
      cursor.execute('''
        INSERT INTO comments (id, task_id, content, created_at)
        VALUES (?, ?, ?, ?)
      ''', (
        comment.id,
        comment.task_id,
        comment.content,
        comment.created_at.isoformat()
      ))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      print(f"Erreur ajout commentaire: {e}")
      return False

  def get_comments_by_task(self, task_id):
    """Récupère tous les commentaires d'une tâche"""

    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments WHERE task_id = ? ORDER BY created_at DESC', (task_id,))
    rows = cursor.fetchall()
    conn.close()

    comments = []
    for row in rows:
      comment = Comment(
        comment_id=row[0],
        task_id=row[1],
        content=row[2],
        created_at=datetime.fromisoformat(row[3])
      )
      comments.append(comment)

    return comments

  def delete_comment(self, comment_id):
    """Supprime un commentaire"""

    try:
      conn = sqlite3.connect(self.db_path)
      cursor = conn.cursor()
      cursor.execute('DELETE FROM comments WHERE id = ?', (comment_id,))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      print(f"Erreur suppression commentaire: {e}")
      return False