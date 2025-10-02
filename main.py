from hashes import *
from globalinfos import *
from sqlitehandler import SQLiteHandler
from upload_window import UploadWindow
from constantes import *
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(purple_theme)
    window = UploadWindow()
    window.show()
    sys.exit(app.exec_())
    filename = input("Le nom du fichier : ")
    datas = {}
    datas["file_name"] = filename
    datas["file_size"] = get_size(filename)
    datas["mime_type"] = get_mime_type(filename)
    datas["creation_time"] = format_timestamp(get_ctime(filename))
    datas["modification_time"] = format_timestamp(get_mtime(filename))
    datas["access_time"] = format_timestamp(get_atime(filename))
    datas["device"] = get_device(filename)
    datas["perms"] = get_perms(filename)
    datas["nlinks"] = get_nblinks(filename)
    datas["uid"] = get_uid(filename)
    datas["gid"] = get_gid(filename)
    datas["md5_hash"] = get_md5(filename)
    datas["sha1_hash"] = get_sha1(filename)
    datas["sha256_hash"] = get_sha256(filename)
    datas["ssdeep_hash"] = get_ssdeep(filename)

    for key, val in datas.items():
        print(f"{key} : {val}")
    