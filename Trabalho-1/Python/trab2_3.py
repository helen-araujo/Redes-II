#Helen Cristina Araujo

#PROBLEMA: Obter informações sobre o IP de seu computador
#SOLUÇÃO: o modulo fornece várias funções e operações que lidam com a 
#criação e manipulação de programas cliente e servidor. Desde modo, utilizamos o
#metodo para buscar o nome do host e em seguida o IP

import socket

meuComputador = socket.gethostname()#busca o nome do computador na rede

meuIP = socket.gethostbyname(meuComputador) #retorna o IP da maquina
print('Nome computador: ')
print(meuComputador)
print('IP :')
print(meuIP)