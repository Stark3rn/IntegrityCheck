from PyQt5.QtCore import QThread, pyqtSignal
from analyzing import get_infos

class AnalyseThread(QThread):
    finished_signal = pyqtSignal(dict)
    error_signal = pyqtSignal(str)

    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def run(self):
        try:
            infos = get_infos(self.filepath)
            self.finished_signal.emit(infos)
        except Exception as e:
            self.error_signal.emit(str(e))
