from flask_bcrypt import Bcrypt

Bcrypt_obj = Bcrypt()

# Encryption
hashed_pass = Bcrypt_obj.generate_password_hash('mysecurepassword')
print(hashed_pass)

# Decrypting
check_wrong = Bcrypt_obj.check_password_hash(hashed_pass, 'wrongpassword')  # checks whether string supplied
# matches with the hashed version of password
print("Status of Password: ", check_wrong)

check_right = Bcrypt_obj.check_password_hash(hashed_pass, 'mysecurepassword')  # matches the password
print("Status of Password: ", check_right)