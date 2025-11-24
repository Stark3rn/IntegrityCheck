DB_PATH = "integritycheck.db"

purple_theme = """
/*
 * Thème Sombre et Moderne avec accents Violets pour PyQt/QSS
 */

/* ===================== Fenêtre principale ===================== */
QMainWindow {
    background-color: #2b2b2b;
    color: #e0e0e0;
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 14px;
}

/* ===================== Labels ===================== */
QLabel {
    color: #cccccc;
    padding: 5px;
}

QLabel#upload_center_label,
QLabel#or_label,
QLabel#filepath_label {
    font-weight: bold;
    color: #bb86fc;
}

/* ===================== Boutons ===================== */
QPushButton {
    background-color: #424242;
    color: #e0e0e0;
    border: 1px solid #555555;
    padding: 10px 20px;
    border-radius: 5px;
    font-weight: bold;
    min-width: 80px;
    outline: none;
}

QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #bb86fc;
    color: #bb86fc;
}

QPushButton:pressed {
    background-color: #383838;
    border: 1px solid #9c27b0;
}

QPushButton:disabled {
    background-color: #333333;
    color: #777777;
    border: 1px solid #444444;
}

/* ===================== Lignes séparatrices ===================== */
QFrame[qproperty-frameShape="4"] { /* 4 = HLine */
    border-top: 1px solid #444444;
    margin: 20px 0;
}

/* ===================== Zones de texte ===================== */
QTextEdit {
    background-color: #333333;
    border: 1px solid #555555;
    border-radius: 5px;
    padding: 10px;
    color: #e0e0e0;
    selection-background-color: #bb86fc;
    selection-color: white;
}

/* ===================== Menu et status bar ===================== */
QMenuBar {
    background-color: #383838;
    color: #e0e0e0;
    border-bottom: 1px solid #444444;
}

QMenuBar::item {
    padding: 5px 10px;
    background-color: transparent;
}

QMenuBar::item:selected {
    background-color: #4a4a4a;
    border-radius: 3px;
}

QStatusBar {
    background-color: #383838;
    color: #e0e0e0;
    border-top: 1px solid #444444;
}

/* ===================== QTreeWidget / QTreeView ===================== */
QTreeWidget, QTreeView {
    background-color: #2b2b2b;
    color: #e0e0e0;
    border: 1px solid #555555;
    font-size: 13px;
    selection-background-color: #bb86fc;
    selection-color: white;
    alternate-background-color: #2f2f2f; /* Ligne alternée */
}

QTreeWidget::item, QTreeView::item {
    padding: 5px;
}

QTreeWidget::item:selected, QTreeView::item:selected {
    background-color: #bb86fc;
    color: #1e1e1e;
}

QTreeWidget::branch:has-children:!has-siblings:closed,
QTreeWidget::branch:closed:has-children,
QTreeWidget::branch:closed:has-children:!has-siblings,
QTreeView::branch:closed:has-children {
    border-image: none;
    image: url(:/icons/arrow-right.png); /* tu peux mettre une icône flèche si tu veux */
}

QTreeWidget::branch:open:has-children,
QTreeWidget::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children {
    border-image: none;
    image: url(:/icons/arrow-down.png);
}

QHeaderView::section {
    background-color: #3a3a3a;
    color: #e0e0e0;
    padding: 4px;
    border: 1px solid #444444;
}

/* ===================== ScrollBars ===================== */
QScrollBar:vertical, QScrollBar:horizontal {
    background-color: #2b2b2b;
    width: 12px;
    height: 12px;
    margin: 0px;
    border: 1px solid #444444;
    border-radius: 5px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #555555;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background-color: #bb86fc;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
}

"""
