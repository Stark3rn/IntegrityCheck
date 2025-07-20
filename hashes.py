import hashlib
import pyssdeep

def get_md5(filename: str):
    """Retourne le hash MD5 d'un fichier"""
    with open(filename, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def get_sha1(filename: str):
    """Retourne le hash SHA1 d'un fichier"""
    with open(filename, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()

def get_sha256(filename: str):
    """Retourne le hash SHA256 d'un fichier"""
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_ssdeep(filename: str):
    """Retourne le fuzzy hash SSDEEP d'un fichier"""
    return pyssdeep.fuzzy_hash_filename(filename)