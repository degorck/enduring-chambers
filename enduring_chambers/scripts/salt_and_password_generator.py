"""
Script to generate random salt and admin password
"""
import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

initial_admin_password = os.getenv("INITIAL_ADMIN_PASSWORD")
password_bytes = initial_admin_password.encode('utf-8')
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password_bytes, salt)
check_password = bcrypt.checkpw(password_bytes, hashed_password)
print("################################### Salt & Password generator ####################################")
print(f'# Initial Admin Password: {initial_admin_password}')
print(f'# Initial Admin Hashed Password: {hashed_password.decode("utf-8")}')
print(f'# Salt: {salt.decode("utf-8")}')
print(f'# Password Check: {check_password}')
print("#################################################################################################")
