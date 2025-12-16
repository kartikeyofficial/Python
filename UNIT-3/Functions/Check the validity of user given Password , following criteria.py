import re  # re module for Regular Expression it is used for matching the condition
def is_valid_password(password):
    if(6<=len(password)<=12 and
       re.search(r'[a-z]',password)and
       re.search(r'[0-9]',password)and
       re.search(r'[A-Z]',password)and
       re.search(r'[$@]',password)):
        return True
    return False

def check_passwords(password):
    password_list= password.split(',')
    valid_passwords=[password for password in password_list if is_valid_password(password)] 
    return ','.join(valid_passwords)
passwords= input("Enter Passwords:")
valid_passwords= check_passwords(passwords)
print("Valid Password: ",valid_passwords)