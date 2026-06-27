from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QListWidget,
    QStackedWidget,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Beaker Pro AI")
        self.resize(1400, 900)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        self.menu = QListWidget()

        self.menu.addItem("💬 AI Chat")
        self.menu.addItem("📄 Documents")
        self.menu.addItem("🧠 Memory")
        self.menu.addItem("🤖 AI Agents")
        self.menu.addItem("🔌 Plugins")
        self.menu.addItem("⚙ Settings")

        self.menu.setFixedWidth(220)

        self.pages = QStackedWidget()

        self.pages.addWidget(self.page("AI Chat"))
        self.pages.addWidget(self.page("Documents"))
        self.pages.addWidget(self.page("Memory"))
        self.pages.addWidget(self.page("AI Agents"))
        self.pages.addWidget(self.page("Plugins"))
        self.pages.addWidget(self.page("Settings"))

        self.menu.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.menu.setCurrentRow(0)

        layout.addWidget(self.menu)
        layout.addWidget(self.pages)

    def page(self, title):
        widget = QWidget()

        layout = QVBoxLayout(widget)

        label = QLabel(title)

        label.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
        """)

        layout.addWidget(label)
        layout.addStretch()

        return widget
