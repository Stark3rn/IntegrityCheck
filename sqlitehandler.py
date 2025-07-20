import sqlite3
import os
from datetime import datetime
from constantes import *

class SQLiteHandler:
    def __init__(self, db_path=DB_PATH):
        self.conn = self.launchDB()
        self.cursor = self.conn.cursor()
        self.create_tables()

    # ==== initialisation functions ====
    def launchDB(self):
        if(not os.path.exists(DB_PATH)):
            print("No DB found. Creating a new one.")

        return sqlite3.connect(DB_PATH)
    
    def create_tables(self):
        # table sources
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,         -- Nom de la source (ex: "Le Monde RSS", "Telegram InfoSec Channel")
            type TEXT NOT NULL,         -- Type de source (ex: "rss", "telegram", "twitter", "web_page")
            url TEXT UNIQUE,            -- URL principale de la source (pour RSS, page Twitter, etc.)
            description TEXT,           -- Description de la source
            last_crawled_at TEXT,       -- Date et heure du dernier crawl (format ISO 8601)
            is_active BOOLEAN DEFAULT 1 -- 1 si la source est active, 0 si désactivée
        )
        ''')
        # table messages
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER NOT NULL,      -- Clé étrangère vers la table 'sources'
            external_id TEXT UNIQUE,         -- ID unique du message dans sa source d'origine (ex: tweet ID, message ID Telegram)
            title TEXT,                      -- Titre du message (pour RSS, articles)
            content TEXT NOT NULL,           -- Contenu principal du message
            url TEXT,                        -- URL directe vers le message/article (si disponible)
            published_at TEXT NOT NULL,      -- Date et heure de publication d'origine (format ISO 8601)
            retrieved_at TEXT NOT NULL,      -- Date et heure à laquelle le message a été récupéré (format ISO 8601)
            author TEXT,                     -- Auteur du message (si disponible)
            language TEXT,                   -- Langue du message (ex: "en", "fr")
            raw_data TEXT,                   -- Champ optionnel pour stocker le JSON/XML brut si nécessaire pour analyse future
            FOREIGN KEY (source_id) REFERENCES sources(id)
        );                    
        ''')

        #table rss_feeds
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS rss_feeds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER NOT NULL UNIQUE, -- Clé étrangère vers la table 'sources'
            feed_url TEXT NOT NULL UNIQUE,     -- URL du flux RSS
            last_item_pub_date TEXT,           -- Date du dernier article publié dans le flux (pour optimisation du crawl)
            FOREIGN KEY (source_id) REFERENCES sources(id)
        );
        ''')

        #table telegram_channels
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS telegram_channels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER NOT NULL UNIQUE,  -- Clé étrangère vers la table 'sources'
            channel_id TEXT NOT NULL UNIQUE,    -- ID numérique ou nom d'utilisateur du channel Telegram
            channel_name TEXT,                  -- Nom du channel (si différent du nom de la source)
            last_message_id INTEGER,            -- ID du dernier message traité dans le channel
            FOREIGN KEY (source_id) REFERENCES sources(id)
        );
        ''')

    # ==== close ====
    def close(self):
        self.conn.close()