print('create account now: ')

username = input('enter username: ')
password = input('enter password: ')

print('you account has been created successfully')
print('Login now! ')

username2 = input('enter username: ')
password2 = input('enter password: ')

if username == username2 and password == password2:
    print('logged in successfully!')
else:
    print('invalid username or password')