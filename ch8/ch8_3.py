password = input('Enter a password: ')
digit = 0
for char in password:
    if char.isdigit():
        digit += 1
digit = 0
if len(password) >= 8 and password.isalnum() and digit >= 2:
    print('valid password')
else:
    print('invalid password')

'''
for i in range(len(password)):
    if password[i].isdigit():
        digit += 1
'''