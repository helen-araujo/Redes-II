#!/bin/bash
#Helen Cristina Araujo

#PROBLEMA: Obter informações sobre seu IP público (IP do NAT)
#SOLUÇÃO: O comando wget irá fazer uma requisição na API ipify que por sua vez retornará o ip publico que estará armazenado no arquivo

wget -qO- https://api.ipify.org > IP_publico.txt  #as informações serão salvas no arquivo
echo 'IP público: ' 
cat IP_publico.txt




