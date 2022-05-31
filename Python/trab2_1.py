#Helen Cristina Araujo

#PROBLEMA: Verificar se a internet está ativa ou não
#SOLUÇÃO Primeiro importamos as bibliotecas necessárias,
#em seguida foi declarada duas variáveis com a url e o tempo maximo da requisicao
#se atender as duas requisições, sinal que a internet esta funcionando.
#Se a função executar, internet funcionando!

#A biblioteca urllib é utilizada para manipular URLs. 
#https://docs.python.org/pt-br/3/library/urllib.html?highlight=urllib
#A biblioteca request é utilizada para fazer requisições HTTP
import urllib
import requests


def verificarConexao():
    url = 'https://www.google.com'
    url1 = 'https://docs.python.org/pt-br/3/'
    timeout = 3

    try:
        #os parametros são da propria função https://docs.python.org/pt-br/3/library/urllib.request.html#module-urllib.request
        urllib.request.urlopen(url, data=None, timeout=timeout, cafile=None, capath=None, cadefault=False, context=None)
        urllib.request.urlopen(url1, data=None, timeout=timeout, cafile=None, capath=None, cadefault=False, context=None)
        return True

    except urllib.error.URLError as err: 
        return False  

if verificarConexao():
    print('Internet OK!')
else:
    print('Sem acesso a internet')
