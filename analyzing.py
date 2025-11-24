from hashes import *
from globalinfos import *
from entropy import *
from yara_scan import *

def format_size(size_bytes):
    if size_bytes == 0:
        return "0 o"
    
    size_name = ("o", "Ko", "Mo", "Go", "To", "Po")
    i = 0
    size = float(size_bytes)
    
    while size >= 1024 and i < len(size_name) - 1:
        size /= 1024
        i += 1
    
    return f"{size:.2f} {size_name[i]}"

def get_infos(filename:str):
    datas = {}
    
    global_infos = {}
    global_infos["file_name"] = filename
    global_infos["file_size"] = format_size(get_size(filename)/1000)
    global_infos["mime_type"] = get_mime_type(filename)
    global_infos["creation_time"] = format_timestamp(get_ctime(filename))
    global_infos["modification_time"] = format_timestamp(get_mtime(filename))
    global_infos["access_time"] = format_timestamp(get_atime(filename))

    metadatas = {}
    metadatas["device"] = get_device(filename)
    metadatas["perms"] = get_perms(filename)
    metadatas["nlinks"] = get_nblinks(filename)
    metadatas["uid"] = get_uid(filename)
    metadatas["gid"] = get_gid(filename)

    hashes = {}
    hashes["md5_hash"] = get_md5(filename)
    hashes["sha1_hash"] = get_sha1(filename)
    hashes["sha256_hash"] = get_sha256(filename)
    hashes["ssdeep_hash"] = get_ssdeep(filename)

    maths = {}
    maths["entropy"] = get_entropy(filename)
    maths["evaluation"] = identification(maths["entropy"])

    yara = scan_file_with_yara(filename)

    datas["global_infos"]=global_infos
    datas["metadatas"]=metadatas
    datas["hash"]=hashes
    datas["maths"]=maths
    datas["yara"]=yara

    return(datas)