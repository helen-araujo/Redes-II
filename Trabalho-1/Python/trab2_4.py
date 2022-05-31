#Helen Cristina Araujo

#PROBLEMA: Obter informações sobre o seu MAC
#SOLUÇÃO: from getmac import get_mac_address as gma
#from getmac import get_mac_address
#import get_mac_address
import socket
import uuid 
import re #expressão regular é uma sequência de caracteres usados 
          #principalmente para encontrar e substituir padrões numa string

print (hex(uuid.getnode())) 
meuMAC = uuid.getnode()
print(meuMAC)
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

#print(gma())
#meuMAC = get_mac_address()
#print("Endereço MAC: "% meuMAC)