#Helen Cristina Araujo

#PROBLEMA: Obter informações sobre seu IP público (IP do NAT)
#SOLUÇÃO: A ipify é uma API de codigo aberto que tem o objetivo de retornar o 
#IP publico após uma requisição. Funciona tanto para IPv4 como para o IPv6.
#A função irá fazer uma requisição do endereço utilizando o requests e o IP será
#armazenado na variável
import requests



def ipPublico():
    meuIPpublico = requests.get('https://api.ipify.org').text
    return meuIPpublico


print('Meu IP publico: ')
print(ipPublico())  