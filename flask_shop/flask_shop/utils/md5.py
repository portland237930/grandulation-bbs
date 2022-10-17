import hashlib
from time import time
def md5_file():
    md5_obj = hashlib.md5()
    md5_obj.update(str(time()).encode())
    file_name = md5_obj.hexdigest()
    return file_name
