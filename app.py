from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def create_folders():

    folders = [
        "logs",
        "cache",
        "plugins",
        "database",
        "assets",
        "documents",
        "voice",
    ]

    for folder in folders:
        Path(folder).mkdir(exist_ok=True)


def main():

    create_folders()

    app = QApplication(sys.argv)
   apply_theme(app)
    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    
    
