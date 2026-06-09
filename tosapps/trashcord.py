import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
import tos 

app = QApplication(sys.argv)

session_path = tos.appdata.path("trashcord")


profile = QWebEngineProfile("Trashcord") 
profile.setPersistentStoragePath(session_path)
profile.setCachePath(os.path.join(session_path, "cache"))
profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)


window = QMainWindow()
window.setWindowTitle(f"Trashcord")
window.resize(1200, 800)


web_view = QWebEngineView()

page = QWebEnginePage(profile, web_view)
web_view.setPage(page)

web_view.load(web_view.url().fromUserInput("https://discord.com/app"))

window.setCentralWidget(web_view)
window.show()

sys.exit(app.exec())