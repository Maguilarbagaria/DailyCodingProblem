#Problem Daily Codin 7 - decode

#OPCIÓN 1 - RECURSSIÓN#El código se puede visualizar muy bien si imaginamos una carretera
#(empieza al principo del string), si dicho principio+el siguiente elemento 
#son menores de 27 (por abecedario) desprendemos otro camino y evaluamos el camino 
#que nos falta hasta al final en busca de más caminos. En caso de no serlo, seguimos avanzando en
#camino en busca de mas caminos. Como si fuera una ramificación. Al llegar al final del camino (a==0), devolvemos 1
#los demás caminos si no encuentran nuevos caminos también terminan sumando +1 al llegar a su final.
#Buscamos en caso de un número inferior a 27 todas las opciones o configuraciones posibles y así sucessivamente:
def decode(num):
    if "0" in num:
        return 'Sorry, 0s are not allowed'
    return decoding(num, len(num))

def decoding(num, a):
    if a == 0:
        return 1
    l = len(num) - a
    rec = decoding(num, a-1)
    if a>1 and int(num[l:l+2])<27:
        rec += decoding(num, a-2)
    return(rec)

print(decode('111'))
print(decode('12121'))
print(decode('3931'))
