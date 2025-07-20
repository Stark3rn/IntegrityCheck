import magic
import os
import datetime
import stat

def get_mime_type(filename:str):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(filename)
    return(mime_type)

def get_size(filename:str):
    """
        retourne la taille du fichier
    """
    return(os.path.getsize(filename))

def get_mtime(filename:str):
    """
        retourne la date de dernière modification du fichier
    """
    return(os.path.getmtime(filename))

def get_ctime(filename:str):
    """
        retourne la date de création du fichier
    """
    return(os.path.getctime(filename))

def get_atime(filename: str):
    """
        retourne la date du dernier accès du fichier.
    """
    return os.path.getatime(filename)

def format_timestamp(ts: float) -> str:
    """
        formatte un timestamp en un format de date lisible
    """
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def get_perms(filename:str):
    stats = os.stat(filename)
    return stat.filemode(stats.st_mode)

def get_nblinks(filename:str):
    stats = os.stat(filename)
    return stats.st_nlink

def get_uid(filename:str):
    stats = os.stat(filename)
    return stats.st_uid

def get_gid(filename:str):
    stats = os.stat(filename)
    return stats.st_gid

def get_device(filename:str):
    stats = os.stat(filename)
    return stats.st_dev