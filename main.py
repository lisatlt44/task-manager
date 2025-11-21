import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow

def main():
  app = QApplication(sys.argv)

  app.setApplicationName("Gestionnaire de Tâches")

  window = MainWindow()
  window.show()

  sys.exit(app.exec())

if __name__ == "__main__":
  main()