import hashlib

def check_pw(password, password_hash):
	return password_hash == hashlib.sha256(password.encode('utf8')).hexdigest()

# Hash password with sha256 and store as hex string
def hash_pw(password)
	return hashlib.sha256(password.encode('utf8')).hexdigest()
