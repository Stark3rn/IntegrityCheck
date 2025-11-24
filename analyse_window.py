from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from constantes import purple_theme

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

        self.setStyleSheet(purple_theme)

        layout.addWidget(self.tree)
        self.setLayout(layout)

        self.tree.itemDoubleClicked.connect(self.copy_value_to_clipboard)
        self.tree.resizeColumnToContents(0)
        self.tree.resizeColumnToContents(1)  

    def copy_value_to_clipboard(self, item, column):
        value = item.text(1)
        if value:
            clipboard = QApplication.clipboard()
            clipboard.setText(value)
            QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), f"Copié dans le presse-papier : {value}", self.tree)