import bcrypt
from dotenv import load_dotenv
import os
load_dotenv()

password = os.getenv("PASSWORD")

bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
salt = os.getenv("SALT").encode('utf-8')
hash = bcrypt.hashpw(bytes, salt)
check_password = bcrypt.checkpw(bytes, hash)
print(hash)
print(salt)
print(check_password)