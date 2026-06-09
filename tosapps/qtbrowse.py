import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QHBoxLayout, QWidget, QLineEdit, QPushButton)
from PyQt6.QtWebEngineWidgets import QWebEngineView

class TrashBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QtBrowse")
        self.resize(1024, 768)

        # Central Widget & Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # --- TOOLBAR (NAV BAR) ---
        self.nav_bar = QWidget()
        self.nav_bar.setStyleSheet("background-color: #222; padding: 5px;")
        self.nav_layout = QHBoxLayout(self.nav_bar)

        # Buttons
        self.back_btn = QPushButton("←")
        self.forward_btn = QPushButton("→")
        self.reload_btn = QPushButton("⟳")
        
        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search...")
        self.url_bar.setStyleSheet("""
            background-color: #333; 
            color: white; 
            border: 1px solid #444; 
            padding: 5px; 
            border-radius: 3px;
        """)

        # Style Buttons
        btn_style = "color: white; background-color: #444; border: none; width: 30px; height: 30px; font-weight: bold;"
        for btn in [self.back_btn, self.forward_btn, self.reload_btn]:
            btn.setStyleSheet(btn_style)

        self.nav_layout.addWidget(self.back_btn)
        self.nav_layout.addWidget(self.forward_btn)
        self.nav_layout.addWidget(self.reload_btn)
        self.nav_layout.addWidget(self.url_bar)

        # --- WEB VIEW ---
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Add to main layout
        self.layout.addWidget(self.nav_bar)
        self.layout.addWidget(self.browser)

        # --- SIGNALS ---
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Global Dark Mode
    app.setStyleSheet("QMainWindow { background-color: #111; }")
    window = TrashBrowser()
    window.show()
    sys.exit(app.exec())