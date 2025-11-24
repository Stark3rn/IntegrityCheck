import hashlib
import pyssdeep

def get_md5(filename: str):
    """returns a file's MD5 hash"""
    with open(filename, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def get_sha1(filename: str):
    """returns a file's SHA1 hash"""
    with open(filename, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()

def get_sha256(filename: str):
    """returns a file's SHA256 hash"""
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_ssdeep(filename: str):
    """returns a file's SSDEEP fuzzy hash"""
    return pyssdeep.fuzzy_hash_filename(filename)