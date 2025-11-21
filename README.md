# Gestionnaire de tâches

Une application desktop pour gérer ses tâches quotidiennes, développée en Python avec PySide6.

## Installation et lancement

1. Cloner le projet
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```
3. Lancer l'application :
```bash
python main.py
```

La base de données SQLite se crée automatiquement au premier lancement dans le dossier `data/`.

## Fonctionnalités

- Créer, modifier et supprimer des tâches
- Ajouter des commentaires aux tâches
- Clôturer une tâche automatiquement
- Filtrer par statut et trier par colonne
- Sauvegarde automatique en base locale

## Comment j'ai organisé le projet

### Architecture MVC

J'ai utilisé le pattern MVC pour séparer les responsabilités :

```
task_manager/
├── models/                     # Classes métiers et gestion des données
│   ├── task.py                 # Modèle Task et énumération TaskStatus
│   ├── comment.py              # Modèle Comment
│   └── database.py             # Couche d'accès SQLite
├── views/                      # Interface utilisateur PySide6
│   ├── ui/                     # Fichiers QtDesigner
│   │   ├── main_window.ui      # Interface principale
│   │   ├── task_dialog.ui      # Dialog tâche
│   │   └── comment_dialog.ui   # Dialog commentaire
│   ├── ui_main_window.py       # Code généré (compilé)
│   ├── ui_task_dialog.py       # Code généré (compilé)
│   ├── ui_comment_dialog.py    # Code généré (compilé)
│   ├── main_window.py          # Logique fenêtre principale
│   ├── task_dialog.py          # Logique dialog tâche
│   └── comment_dialog.py       # Logique dialog commentaire
├── controllers/                # Logique métier
│   └── task_controller.py      # Contrôleur principal
├── utils/                      # Fonctions utilitaires
│   ├── validators.py           # Validation des données
│   └── dialogs.py              # Utilitaires d'interface
├── data/                       # Base de données SQLite
│   └── tasks.db                # Fichier créé automatiquement
├── main.py                     # Point d'entrée
├── requirements.txt            # Dépendances Python
└── README.md                   # Documentation
```

**Pourquoi cette organisation ?**
- Les **models** s'occupent uniquement des données
- Les **views** gèrent l'affichage sans logique métier
- Le **controller** fait le lien entre les deux
- C'est plus facile à maintenir et à débugger

### Rôles détaillés

#### Modèles (`models/`)
- **`task.py`** : Classe Task avec ses attributs + énumération TaskStatus (5 états)
- **`comment.py`** : Classe Comment avec contenu et timestamp
- **`database.py`** : Couche d'accès aux données SQLite (CRUD complet)

#### Vues (`views/`)
- **`main_window.py`** : Fenêtre principale avec tableau des tâches
- **`task_dialog.py`** : Dialog de création/modification de tâche
- **`comment_dialog.py`** : Dialog d'ajout de commentaire
- **`ui/`** : Fichiers QtDesigner (.ui) et compilations Python

#### Contrôleurs (`controllers/`)
- **`task_controller.py`** : Logique métier, validation, orchestration entre modèles et vues

### Choix techniques

#### SQLite plutôt que JSON
Au début j'hésitais entre SQLite et JSON. J'ai choisi **SQLite** parce que :
- Les relations tâches <=> commentaires sont plus propres à gérer
- La suppression en cascade fonctionne automatiquement
- Pas besoin de charger tout en mémoire
- Plus rapide pour trier et filtrer

#### Gestion des relations (tâche → commentaires)

**En base de données :**
- Table `tasks` : stockage des tâches
- Table `comments` : stockage des commentaires avec clé étrangère vers `tasks`
- Contrainte `FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE`

**En mémoire :**
- Chaque `Task` a une liste `comments` chargée depuis la base
- Relation 1-N (une tâche peut avoir plusieurs commentaires)

#### PySide6 avec QtDesigner
- Interface graphique native et moderne
- QtDesigner pour le design visuel
- Compilation en Python pour l'intégration

#### Style Apple-like
J'ai voulu faire quelque chose de moderne, inspiré du design Apple avec des bordures arrondies.

## Comment ça marche techniquement

### Les modèles de données

**Une tâche** a :
- Un titre (obligatoire)
- Une description (optionnelle) 
- Des dates de début/fin (optionnelles)
- Un statut parmi : À faire, En cours, Réalisé, Abandonné, En attente
- Une liste de commentaires

**Un commentaire** a :
- Du contenu (obligatoire)
- Une date de création automatique
- L'ID de la tâche parente

### La validation

J'ai mis des validations pour éviter les erreurs :
- **Titre** : minimum 3 caractères, maximum 200
- **Description** : maximum 1000 caractères  
- **Dates** : la fin doit être après le début
- **Commentaires** : pas vides, maximum 500 caractères

Si une validation échoue, un message d'erreur s'affiche et le dialog ne se ferme pas.

#### Comportement en cas d'erreurs
- **Messages clairs** : QMessageBox avec description de l'erreur
- **Blocage** : Les dialogs ne se ferment pas tant que les données sont invalides
- **Feedback visuel** : Focus automatique sur les champs en erreur
- **Exceptions** : Try/catch sur les opérations base de données

### La clôture de tâche

Fonctionnalité spéciale demandée dans le projet :
1. Bouton "Clôturer" dans l'interface principale
2. Vérification qu'une tâche est sélectionnée
3. Confirmation utilisateur
4. Passage automatique en statut "Réalisé"
5. Date de fin définie à aujourd'hui si elle était vide

## Les défis rencontrés

### Synchroniser l'interface et la base

Au début, quand je modifiais une tâche, les changements n'apparaissaient pas tout de suite dans le tableau. J'ai dû gérer le rafraichissement de l'interface après chaque opération.

### Gestion des relations en SQLite

Faire en sorte que quand on supprime une tâche, tous ses commentaires se suppriment aussi.

### Interface responsive

Faire en sorte que l'interface soit réactive et intégrer tous les messages de confirmation etc.

### Style cohérent

Appliquer un style moderne sans framework CSS. J'ai utilisé les StyleSheets de Qt directement dans QtDesigner.

## Ce que j'ai appris

Ce projet m'a permis de découvrir :
- **PySide6** et l'écosystème Qt
- **SQLite** avec les relations et contraintes
- **Le design d'interface**
- **L'importance de la validation**

Le plus satisfaisant a été de voir l'app prendre forme progressivement et devenir vraiment utilisable.

## Améliorations possibles

J'aurais pu ajouté :
- **Recherche textuelle** dans les tâches
- **Export** en CSV ou PDF
- **Notifications** pour les échéances

Mais l'essentiel est là et fonctionne bien !

## Technologies utilisées

- **Python 3.11**
- **PySide6** (interface graphique)
- **SQLite** (base de données)
- **QtDesigner** (design d'interface)
