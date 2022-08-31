import hashlib
message = "Some text to hash".encode()
print("SHA-512:", hashlib.sha256(message).hexdigest())