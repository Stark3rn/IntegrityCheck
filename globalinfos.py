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
        returns file size (in bytes)
    """
    return(os.path.getsize(filename))

def get_mtime(filename:str):
    """
        return file's last modification time
    """
    return(os.path.getmtime(filename))

def get_ctime(filename:str):
    """
        return file's creation time
    """
    return(os.path.getctime(filename))

def get_atime(filename: str):
    """
        return file's last access time
    """
    return os.path.getatime(filename)

def format_timestamp(ts: float) -> str:
    """
        formats a timestamp into a human-readable format
    """
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def get_perms(filename:str):
    """
        returns a file's permissions
    """
    stats = os.stat(filename)
    return stat.filemode(stats.st_mode)

def get_nblinks(filename:str):
    """
        returns the number of links a file has
    """
    stats = os.stat(filename)
    return stats.st_nlink

def get_uid(filename:str):
    """
        returns the file's owner uid
    """
    stats = os.stat(filename)
    return stats.st_uid

def get_gid(filename:str):
    """
        returns the file's owner gid
    """
    stats = os.stat(filename)
    return stats.st_gid

def get_device(filename:str):
    stats = os.stat(filename)
    return stats.st_dev

def is_file(filename:str):
    """
        returns true if the path corresponds to a file
    """
    return os.path.isfile(filename)

def is_dir(filename:str):
    """
        returns true if the path corresponds to a directory
    """
    return os.path.isdir(filename)

def is_link(filename:str):
    """
        returns true if the path corresponds to a file link
    """
    return os.path.islink(filename)