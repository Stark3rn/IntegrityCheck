from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox
from constantes import purple_theme
from export import export_json, export_md
import os

def add_dict_to_tree(parent_item, data: dict):
    for key, value in data.items():
        if isinstance(value, dict):
            node = QtWidgets.QTreeWidgetItem([str(key), ""])
            parent_item.addChild(node)
            add_dict_to_tree(node, value)
        else:
            child = QtWidgets.QTreeWidgetItem([str(key), str(value)])
            parent_item.addChild(child)

class AnalyseWindow(QtWidgets.QWidget):
    def __init__(self, infos: dict):
        super().__init__()
        self.setWindowTitle("Analyse du fichier")
        self.resize(900, 600)

        layout = QtWidgets.QVBoxLayout()

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["Names", "Values"])
        self.tree.header().setStretchLastSection(True)

        root = QtWidgets.QTreeWidgetItem(["Analyse Results", ""])
        self.tree.addTopLevelItem(root)

        add_dict_to_tree(root, infos)
        self.tree.expandAll()

        self.export_json_button = QtWidgets.QPushButton()
        self.export_json_button.setMinimumSize(QtCore.QSize(300, 0))
        self.export_json_button.setMaximumSize(QtCore.QSize(400, 16777215))
        self.export_json_button.setObjectName("export_json_button")
        _translate = QtCore.QCoreApplication.translate
        self.export_json_button.setText(_translate("AnalyseWindow", "Export to JSON"))
        self.export_json_button.clicked.connect(self.export_datas_to_json)

        self.export_md_button = QtWidgets.QPushButton()
        self.export_md_button.setMinimumSize(QtCore.QSize(300, 0))
        self.export_md_button.setMaximumSize(QtCore.QSize(400, 16777215))
        self.export_md_button.setObjectName("export_md_button")
        _translate = QtCore.QCoreApplication.translate
        self.export_md_button.setText(_translate("AnalyseWindow", "Export to MD"))
        self.export_md_button.clicked.connect(self.export_datas_to_md)


        self.setStyleSheet(purple_theme)

        layout.addWidget(self.tree)
        layout.addWidget(self.export_json_button)
        layout.addWidget(self.export_md_button)
        self.setLayout(layout)

        self.tree.itemDoubleClicked.connect(self.copy_value_to_clipboard)
        self.tree.resizeColumnToContents(0)
        self.tree.resizeColumnToContents(1)

        self.infos = infos

    def copy_value_to_clipboard(self, item, column):
        value = item.text(1)
        if value:
            clipboard = QApplication.clipboard()
            clipboard.setText(value)
            QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), f"Copied to clipboard : {value}", self.tree)

    def export_datas_to_json(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Export JSON",
            "",
            "JSON File (*.json);;All Files (*)"
        )

        if not filepath:
            QtWidgets.QMessageBox.warning(self, "Cancelled", "Export cancelled.")
            return

        if os.path.splitext(filepath)[-1] != ".json":
            filepath += ".json"

        result = export_json(self.infos, filepath)

        if result[0] == 0:
            QtWidgets.QMessageBox.information(self, "Success", "Exported file!")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", f"Cannot export file : {result[1]}")

    
    def export_datas_to_md(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Export Markdown",
            "",
            "Markdown File (*.md);;All Files (*)"
        )

        if not filepath:
            QtWidgets.QMessageBox.warning(self, "Cancelled", "Export cancelled.")
            return

        print(os.path.splitext(filepath)[-1])

        if os.path.splitext(filepath)[-1] != ".md":
            filepath += ".md"

        result = export_md(self.infos, filepath)

        if result[0] == 0:
            QtWidgets.QMessageBox.information(self, "Success", "Exported file!")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", f"Cannot export file : {result[1]}")
