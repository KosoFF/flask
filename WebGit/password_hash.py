import hashlib

def generate_password_hash(password):
    h = hashlib.md5()
    h.update (password)
    return h.hexdigest()
def check_password_hash(password_hash, password):
    h = hashlib.md5()
    h.update(password)
    return h.hexdigest() == password