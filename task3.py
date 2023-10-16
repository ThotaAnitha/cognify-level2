import re
def password_validator(password):
    if len(password) < 8:
        return Flase
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[!@#$%^&*().?":{}|<>]',password):
        return False
    return True
password = input("input your password:")
pass_valid = password_validator(password)
if pass_valid:
    print("your password is valid .")
else:
    print("your password is not valid.")
