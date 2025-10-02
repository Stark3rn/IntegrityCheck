DB_PATH = "integritycheck.db"

purple_theme = """
/*
 * Thème Sombre et Moderne avec accents Violets pour PyQt/QSS
 */

/* Style général de la fenêtre */
QMainWindow {
    background-color: #2b2b2b; /* Gris très foncé pour le fond principal */
    color: #e0e0e0; /* Texte clair pour un bon contraste */
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 14px;
}

/* Style des labels */
QLabel {
    color: #cccccc; /* Gris clair pour les labels */
    padding: 5px;
}

/* Labels de titre ou importants (comme "Drag & Drop file", "OR", "No File Uploaded") */
QLabel#upload_center_label,
QLabel#or_label,
QLabel#filepath_label {
    font-weight: bold;
    color: #bb86fc; /* Violet vif pour les accents et titres */
}

/* Style des boutons */
QPushButton {
    background-color: #424242; /* Gris foncé pour le fond du bouton */
    color: #e0e0e0; /* Texte clair sur les boutons */
    border: 1px solid #555555; /* Bordure subtile */
    padding: 10px 20px;
    border-radius: 5px;
    font-weight: bold;
    min-width: 80px;
    outline: none; /* Supprime le contour de focus par défaut */
}

QPushButton:hover {
    background-color: #4a4a4a; /* Gris légèrement plus clair au survol */
    border: 1px solid #bb86fc; /* Bordure violette au survol */
    color: #bb86fc; /* Texte violet au survol */
}

QPushButton:pressed {
    background-color: #383838; /* Gris plus foncé au clic pour un effet "enfoncé" */
    border: 1px solid #9c27b0; /* Violet plus foncé au clic */
}

QPushButton:disabled {
    background-color: #333333; /* Gris très foncé pour les boutons désactivés */
    color: #777777; /* Texte gris estompé */
    border: 1px solid #444444;
}

/* Ligne séparatrice */
QFrame[qproperty-frameShape="4"] { /* 4 correspond à HLine */
    border-top: 1px solid #444444; /* Ligne fine gris foncé */
    margin: 20px 0; /* Plus de marge verticale pour l'espace */
}

/* Zone de texte (pour l'affichage des résultats d'analyse) */
QTextEdit {
    background-color: #333333; /* Fond gris foncé pour la zone de texte */
    border: 1px solid #555555; /* Bordure gris moyen */
    border-radius: 5px;
    padding: 10px;
    color: #e0e0e0; /* Texte clair */
    selection-background-color: #bb86fc; /* Violet vif pour la sélection */
    selection-color: white; /* Texte blanc sur fond violet sélectionné */
}

/* Barres de menu et de statut */
QMenuBar {
    background-color: #383838; /* Gris foncé pour la barre de menu */
    color: #e0e0e0;
    border-bottom: 1px solid #444444; /* Petite séparation */
}

QMenuBar::item {
    padding: 5px 10px;
    background-color: transparent;
}

QMenuBar::item:selected {
    background-color: #4a4a4a; /* Gris légèrement plus clair au survol des items */
    border-radius: 3px;
}

QStatusBar {
    background-color: #383838;
    color: #e0e0e0;
    border-top: 1px solid #444444;
}
"""