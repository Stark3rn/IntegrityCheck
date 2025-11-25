import sqlite3
from datetime import datetime

#
#       DB INIT FUNCTION
#

def open_or_create_db(filename:str)->sqlite3.Connection:
    """
    Nom : open_or_create_db
    Desc : if the file exists, open the database. Else, it create it.
    Return : sqlite3.Connection of the db
    """

    if not filename.endswith(".db"):
        filename += ".db"

    connection = sqlite3.connect(filename)
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection

#
#       TABLE CREATION FUNCTIONS
#

def create_scan_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_scan_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `scan`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scan ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        date DATETIME
                        );""")
    connection.commit()  

def create_global_info_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_global_info_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `global_info`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS global_info ( 
                        id_scan INTEGER PRIMARY KEY, 
                        file_name TEXT,
                        file_size REAL,
                        mime_type TEXT,
                        creation_time TEXT,
                        modification_time TEXT,
                        access_time TEXT,
                        FOREIGN KEY (id_scan) REFERENCES scan(id)
                        );""")
    connection.commit()  

def create_metadata_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_metadata_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `metadata`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS metadata ( 
                        id_scan INTEGER PRIMARY KEY, 
                        device INT,
                        perms TEXT,
                        nlinks INT,
                        uid INT,
                        gid INT,
                        FOREIGN KEY (id_scan) REFERENCES scan(id)
                        );""")
    connection.commit()  

def create_hash_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_hash_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `hash`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS hash ( 
                        id_scan INTEGER PRIMARY KEY, 
                        md5_hash TEXT,
                        sha1_hash TEXT,
                        sha256_hash TEXT,
                        ssdeep_hash TEXT,
                        FOREIGN KEY (id_scan) REFERENCES scan(id)
                        );""")
    connection.commit()  

def create_math_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_math_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `math`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS math ( 
                        id_scan INTEGER PRIMARY KEY, 
                        entropy REAL,
                        evaluation TEXT,
                        FOREIGN KEY (id_scan) REFERENCES scan(id)
                        );""")
    connection.commit()

def create_yara_file_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_yara_file_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `yara_file`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS yara_file ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_scan INTEGER,
                        file_name TEXT,
                        FOREIGN KEY(id_scan) REFERENCES scan(id)
                        );""")
    connection.commit()

def create_yara_rule_table(connection:sqlite3.Connection)->None:
    """
    Nom : create_yara_file_table
    Args: 
        - connection (type `sqlite3.Connection`) : connection made to your database
    Desc : Creates the table called `yara_file`.
    Return : Nothing
    """
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS yara_rule ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_yara_file INTEGER,
                        rule_name TEXT,
                        FOREIGN KEY(id_yara_file) REFERENCES yara_file(id)
                        );""")
    connection.commit()

def init_tables(db_path:str):
    """
    Nom : init_tables
    Args:
        - db_path (type `str`) : path of the database
    Desc : Creates all the tables necessary for the history (if they don't exists).
    Return : nothing
    """
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    create_scan_table(conn)
    create_global_info_table(conn)
    create_metadata_table(conn)
    create_hash_table(conn)
    create_math_table(conn)
    create_yara_file_table(conn)
    create_yara_rule_table(conn)
    conn.close()

#
#       DB GET FUNCTIONS
#

def get_scan(conn: sqlite3.Connection, scan_id: int) -> dict:
    """
    Nom : get_scan
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
    Desc : Get the scans infos by scan_id.
    Return : dict
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id, date FROM scan WHERE id = ?", (scan_id,))
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "date": row[1]}
    return {}

def get_global_infos(conn: sqlite3.Connection, id_scan: int) -> dict:
    """
    Nom : get_global_infos
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
    Desc : Get all the global information of a scan.
    Return : dict
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT file_name, file_size, mime_type, creation_time, modification_time, access_time
        FROM global_info
        WHERE id_scan = ?
    """, (id_scan,))
    row = cursor.fetchone()
    if row:
        return {
            "file_name": row[0],
            "file_size": row[1],
            "mime_type": row[2],
            "creation_time": row[3],
            "modification_time": row[4],
            "access_time": row[5]
        }
    return {}


def get_metadata(conn: sqlite3.Connection, id_scan: int) -> dict:
    """
    Nom : get_metadata
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
    Desc : Get the metadata infos by scan_id.
    Return : dict
    """
    cursor = conn.cursor()
    cursor.execute("SELECT device, perms, nlinks, uid, gid FROM metadata WHERE id_scan = ?", (id_scan,))
    row = cursor.fetchone()
    if row:
        return {
            "device": row[0],
            "perms": row[1],
            "nlinks": row[2],
            "uid": row[3],
            "gid": row[4]
        }
    return {}



def get_yara(conn:sqlite3.Connection,id_scan:int)-> dict:
    """
    Nom : get_yara
    Args:
        - conn (type `sqlite3.Connection`) : connection to the database
        - id_scan (type : `int`) : id of the file scan
    Desc : Get all the yara file-rules triggered.
    Return : dict
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_name FROM yara_file WHERE id_scan = ?", (id_scan,))
    yara_files = cursor.fetchall()

    yara = {}
    for yara_file_id, file_name in yara_files:
        cursor.execute("SELECT rule_name FROM yara_rule WHERE id_yara_file = ?", (yara_file_id,))
        rules = [row[0] for row in cursor.fetchall()]
        yara[file_name] = rules

    return yara

def get_hash(conn: sqlite3.Connection, id_scan: int) -> dict:
    """
    Nom : get_hash
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
    Desc : Get the hash infos by scan_id.
    Return : dict
    """
    cursor = conn.cursor()
    cursor.execute("SELECT md5_hash, sha1_hash, sha256_hash, ssdeep_hash FROM hash WHERE id_scan = ?", (id_scan,))
    row = cursor.fetchone()
    if row:
        return {
            "md5_hash": row[0],
            "sha1_hash": row[1],
            "sha256_hash": row[2],
            "ssdeep_hash": row[3]
        }
    return {}

def get_math(conn: sqlite3.Connection, id_scan: int) -> dict:
    """
    Nom : get_math
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
    Desc : Get the math infos by scan_id.
    Return : dict
    """
    cursor = conn.cursor()
    cursor.execute("SELECT entropy, evaluation FROM math WHERE id_scan = ?", (id_scan,))
    row = cursor.fetchone()
    if row:
        return {"entropy": row[0], "evaluation": row[1]}
    return {}


#
#       DB INSERT FUNCTIONS
#

def insert_scan(conn: sqlite3.Connection, date: str = datetime.now()) -> int:
    """
    Nom : insert_scan
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
    Desc : add a scan to the `scan` table.
    Return : int (id_scan)
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scan (date) VALUES (?)", (date,))
    conn.commit()
    return cursor.lastrowid

def insert_global_infos(conn:sqlite3.Connection,id_scan:int,file_name:str,file_size:float,mime_type:str,creation_time: str,modification_time: str,access_time:str):
    """
    Nom : insert_global_infos
    Args:
        - conn (type `sqlite3.Connection`) : connection to the database
        - id_scan (type : `int`) : id of the file scan
        - file_name (type : `str`) : name of the file
        - file_size (type : `float`) : size of the file (in bytes)
        - mime_type (type : `str`) : mime type of the file
        - creation_time (type : `str`) : creation date of the file
        - modification_time (type : `str`) : last modification time of the file
        - access_time (type : `str`) : last access time of the file
    Desc : Add global infos for a scan
    Return : nothing
    """
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO global_info (
            id_scan, file_name, file_size, mime_type, creation_time, modification_time, access_time
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (id_scan, file_name, file_size, mime_type, creation_time, modification_time, access_time))
    
    conn.commit()

def insert_metadata(conn: sqlite3.Connection, id_scan: int, device: int, perms: str, nlinks: int, uid: int, gid: int):
    """
    Nom : insert_metadata
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
        - device (int) : 
        - perms (str) : permissions of the file
        - nlinks (int) : number of links for the file
        - uid (int) : uid associated to the file owner
        - gid (int) : gid associated to the file's group owner
    Desc : add metadata for a scan.
    Return : nothing
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO metadata (id_scan, device, perms, nlinks, uid, gid)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (id_scan, device, perms, nlinks, uid, gid))
    conn.commit()

def insert_hash(conn: sqlite3.Connection, id_scan: int, md5_hash: str, sha1_hash: str, sha256_hash: str, ssdeep_hash: str):
    """
    Nom : insert_hash
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
        - md5_hash (str) : md5 hash of the file
        - sha1_hash (str) : sha1 hash of the file
        - sha256_hash (str) : sha256 hash of the file
        - ssdeep_hash (str) : ssdeep fuzzy hash of the file
    Desc : add hash infos for a scan.
    Return : nothing
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO hash (id_scan, md5_hash, sha1_hash, sha256_hash, ssdeep_hash)
        VALUES (?, ?, ?, ?, ?)
    """, (id_scan, md5_hash, sha1_hash, sha256_hash, ssdeep_hash))
    conn.commit()

def insert_math(conn: sqlite3.Connection, id_scan: int, entropy: float, evaluation: str):
    """
    Nom : insert_math
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
        - entropy (float) : entropy of the file
        - evaluation (str) : evalutation given for the file
    Desc : add math infos for a scan.
    Return : nothing
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO math (id_scan, entropy, evaluation)
        VALUES (?, ?, ?)
    """, (id_scan, entropy, evaluation))
    conn.commit()

def insert_yara_file(conn: sqlite3.Connection, id_scan: int, file_name: str):
    """
    Nom : insert_yara_file
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_scan (int) : id of the file scan
        - file_name (str) : name the yara rule file
    Desc : add yara file infos for a scan.
    Return : nothing
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO yara_file (id_scan, file_name)
        VALUES (?, ?)
    """, (id_scan, file_name))
    conn.commit()
    return cursor.lastrowid


def insert_yara_rule(conn: sqlite3.Connection, id_yara_file: int, rule_name: str):
    """
    Nom : insert_yara_rule
    Args:
        - conn (sqlite3.Connection) : connection to the database
        - id_yara_file (int) : id of the yara file connected to a scan
        - rule_name (str) : name the yara rule
    Desc : add yara rule infos for a scan.
    Return : nothing
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO yara_rule (id_yara_file, rule_name)
        VALUES (?, ?)
    """, (id_yara_file, rule_name))
    conn.commit()