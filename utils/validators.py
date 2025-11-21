class TaskValidator:
  """Pour vérifier que les données des tâches sont correctes"""

  @staticmethod
  def validate_title(title):
    """Vérifie que le titre est valide"""

    # Le titre ne peut pas être vide
    if not title or not title.strip():
      return False, "Le titre est obligatoire"

    # Au moins 3 caractères
    if len(title.strip()) < 3:
      return False, "Le titre doit contenir au moins 3 caractères"

    # Pas trop long
    if len(title) > 200:
      return False, "Le titre ne peut pas dépasser 200 caractères"

    return True, ""

  @staticmethod
  def validate_dates(start_date, end_date):
    """Vérifie que les dates sont cohérentes"""

    # Si on a les deux dates, la fin doit être après le début
    if start_date and end_date:
      if end_date < start_date:
        return False, "La date de fin doit être après la date de début"

    return True, ""

  @staticmethod
  def validate_description(description):
    """Vérifie la description"""

    # Pas trop long
    if description and len(description) > 1000:
      return False, "La description ne peut pas dépasser 1000 caractères"

    return True, ""

class CommentValidator:
  """Pour vérifier que les commentaires sont corrects"""

  @staticmethod
  def validate_content(content):
    """Vérifie que le commentaire est valide"""

    # Le commentaire ne peut pas être vide
    if not content or not content.strip():
      return False, "Le commentaire ne peut pas être vide"

    # Pas trop long
    if len(content) > 500:
      return False, "Le commentaire ne peut pas dépasser 500 caractères"

    return True, ""