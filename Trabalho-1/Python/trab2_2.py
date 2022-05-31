#Helen Cristina Araujo

#PROBLEMA: Calcular quanto tempo para fazer uma requisição no site http://www.google.com
#SOLUÇÃO: Foi criada a função requisiçãoHTTP para fazer a requisição no Google. 
#Foi utilizada a biblioteca timeit para capturar o tempo em que a função demorou para fazer a requisicao.
#Se ao inves de criar a função fosse feita a requisição direto, o tempo seria milessemos a menos que o inicial

import urllib
import requests
import timeit


def requisicaoHTTP():
    response = requests.get('https://www.google.com')
    #print(response.status_code)
    #print(response.headers)
    return True 


tempoInicial = timeit.default_timer() #mede o tempo real em 1/60 segundos
requisicaoHTTP()
tempoFim = timeit.default_timer()
print(tempoInicial)
print(tempoFim)
print ('Tempo Gasto: %f' % (tempoFim - tempoInicial))



