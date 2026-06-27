from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

def apply_theme(app):
    palette = QPalette()

    palette.setColor(QPalette.Window, QColor("#202124"))
    palette.setColor(QPalette.WindowText, Qt.white)

    palette.setColor(QPalette.Base, QColor("#2B2B2B"))
    palette.setColor(QPalette.AlternateBase, QColor("#323232"))

    palette.setColor(QPalette.Button, QColor("#2F80ED"))
    palette.setColor(QPalette.ButtonText, Qt.white)

    palette.setColor(QPalette.Text, Qt.white)

    palette.setColor(QPalette.Highlight, QColor("#2F80ED"))
    palette.setColor(QPalette.HighlightedText, Qt.white)

    app.setPalette(palette)
