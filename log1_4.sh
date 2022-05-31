#!/bin/bash
#Helen Cristina Araujo

#PROBLEMA: Obter informações sobre o seu MAC
#SOLUÇÃO: Segue a mesma logica do exercicio anterior. O ifconfig irá buscar informações relevantes a rede que será armazenadas em um arquivo. Por ultimo, será feita a busca no arquivo pelas informações sobre o MAC

ifconfig > infRedeMAC.txt # O comando ifconfig lista varias informações da rede. E será armazenado no arquivo
cat infRedeMAC.txt | grep inet # O comando cat irá exibir o arquvo, e o comando grep irá buscar todas as linhas que contem 'ether' no qual fica o IP
echo -e "MAC informado!"




