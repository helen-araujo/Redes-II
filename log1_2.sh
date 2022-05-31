#!/bin/bash
#Helen Cristina Araujo

#PROBLEMA: Calcular quanto tempo para fazer uma requisição no site http://www.google.com
#SOLUÇÃO: o traceroute irá imprimir a rota ate chegar ao servidor em que esta o endereço Google. Em cada host tem o IP e o tempo gasto. A ultima rota - no qual está o destino possui o tempo gasto na requisiçã

traceroute www.google.com > tempo.txt   # a rota completa estará salva no arquivo tempo.txt.
cat tempo.txt | tail -1 # Time irá armezanar a ultima rota
echo Calculo feito! Veja o arquivo tempo.txt



