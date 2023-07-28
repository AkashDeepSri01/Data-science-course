uname= "Admin"
pwd=  "admin123"
while True:
    username=input('enter name:')
    password =input('enter password:')
    if username !=uname:
        print('😡invalid username')
    if password != pwd:
        print('😡invalid password')
    if username == uname and password==pwd:
        print('🤑login succesfull')        
        break
