#!/bin/bash
#Helen Cristina Araujo

#PROBLEMA: Verificar se a internet está ativa ou não
#SOLUÇÃO: o ping irá fazer uma requisição no servidor do google e salvar no arquivo. Se funcionar a internet esta ativa

if ping -c 1 www.google.com > ping.txt; #O -c e o 1 garante que seja feita apenas uma requisição
 then 

    echo Internet Ok
else
    echo Sem acesso a internet
fi	


