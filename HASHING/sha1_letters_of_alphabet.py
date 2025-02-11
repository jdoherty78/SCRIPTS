import hashlib


alphabet = 'abcdefghijklmnopqrstuvwxyz'


for letter in alphabet:
    
    sha1_hash = hashlib.sha1()
        
    sha1_hash.update(letter.encode('utf-8'))
    
    hex_digest = sha1_hash.hexdigest()
    
    print(f"Letter: {letter}, SHA-1: {hex_digest}")