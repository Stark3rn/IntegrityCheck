from upload_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class UploadWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img/app_icon.png'))

        # Activer le drag & drop
        self.setAcceptDrops(True)
        # File browser avec le bouton
        self.ui.upload_button.clicked.connect(self.browse_file)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            print(f"Fichier déposé : {file_path}")
            self.ui.filepath_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Fichier : {file_path}</span></p></body></html>")

    def browse_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Sélectionner un fichier")
        if file_path:
            print(f"Fichier sélectionné : {file_path}")
            self.ui.filepath_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Fichier : {file_path}</span></p></body></html>")