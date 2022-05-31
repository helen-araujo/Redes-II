#!/bin/bash
#Helen Cristina Araujo

#PROBLEMA: Obter informações sobre o IP de seu computador
#SOLUÇÃO: o comando ifconfig retorna varias informações relevantes sobre a rede, inclusive o IP. Estas informações serao salvas no arquivo infRede.txt

ifconfig > infRede.txt # O comando ifconfig lista varias informações da rede. E será armazenado no arquivo
cat infRede.txt | grep inet # O comando cat irá exibir o arquvo, e o comando grep irá buscar todas as linhas que contem 'ether' no qual fica o IP
echo -e "IP informado!"

