from hashes import *
from globalinfos import *
from upload_window import UploadWindow
from constantes import *
import sys
from analyzing import *
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(purple_theme)
    window = UploadWindow()
    window.show()
    sys.exit(app.exec_())
    filename = input("Le nom du fichier : ")
    
    datas = get_infos(filename)
    
    for key, val in datas.items():
        print(f"{key} : {val}")