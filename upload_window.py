from upload_ui import Ui_MainWindow
from analyse_window import AnalyseWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from analyse_thread import AnalyseThread

class UploadWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('img/app_icon.png'))
        self.setAcceptDrops(True) # drag & drop

        self.ui.upload_button.clicked.connect(self.browse_file)
        self.ui.analyse_button.clicked.connect(self.analyse_file)

        self.loaded_file = None # link to the file to analyse

        self.loading_label = QtWidgets.QLabel(self)
        self.loading_label.setGeometry(0, 0, self.width(), self.height())  
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setVisible(False)
        self.loading_label.setScaledContents(True)  

        self.movie = QtGui.QMovie("img/loading.gif")
        self.loading_label.setMovie(self.movie)

    # ----------------------------------------------------------------------
    #  DRAG & DROP
    # ----------------------------------------------------------------------
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.set_file_path(file_path)

    # ----------------------------------------------------------------------
    #  BROWSE BUTTON
    # ----------------------------------------------------------------------
    def browse_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Sélectionner un fichier")
        if file_path:
            self.set_file_path(file_path)

    # ----------------------------------------------------------------------
    #  PRINT PATH IN UI
    # ----------------------------------------------------------------------
    def set_file_path(self, file_path):
        self.loaded_file = file_path
        self.ui.filepath_label.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">"
            f"Fichier : {file_path}</span></p></body></html>"
        )

    # ----------------------------------------------------------------------
    #  OPEN ANALYSE WINDOW
    # ----------------------------------------------------------------------
    def analyse_file(self):
        if not self.loaded_file:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Aucun fichier sélectionné.")
            return
        
        self.loading_label.setVisible(True)
        self.movie.start()

        # Creates the thread
        self.thread = AnalyseThread(self.loaded_file)
        self.thread.finished_signal.connect(self.on_analysis_done)
        self.thread.error_signal.connect(self.on_analysis_error)
        self.thread.start()

    def on_analysis_done(self, infos):
        self.movie.stop()
        self.loading_label.setVisible(False)
        self.analysis_window = AnalyseWindow(infos)
        self.analysis_window.show()
        self.thread = None 

    def on_analysis_error(self, message):
        self.movie.stop()
        self.loading_label.setVisible(False)
        QtWidgets.QMessageBox.critical(self, "Erreur lors de l'analyse", message)
        self.thread = None
