import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
import tos 
is_root = tos.is_root()
if is_root == True:
    print("SECURITY WARNING")
    print("Running as root is dangerous!!")

app = QApplication(sys.argv)

session_path = tos.appdata.path("trashtubex")


profile = QWebEngineProfile("Trashcord") 
profile.setPersistentStoragePath(session_path)
profile.setCachePath(os.path.join(session_path, "cache"))
profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)


window = QMainWindow()
window.setWindowTitle(f"Trashtube X")
window.resize(1200, 800)


web_view = QWebEngineView()

page = QWebEnginePage(profile, web_view)
web_view.setPage(page)

web_view.load(web_view.url().fromUserInput("https://youtube.com/"))

window.setCentralWidget(web_view)
window.show()

sys.exit(app.exec())