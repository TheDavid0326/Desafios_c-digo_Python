"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

#Solución 1
def es_anagrama(palabra_1,palabra_2):
    list_palabra_2=[]
    anagrama="No es un anagrama"
    for i in palabra_2:
        list_palabra_2.append(i)
    
    for count, valor in enumerate(palabra_2):
        #print(count, valor)
        letra_encontrada=False
        for i in palabra_1:
            if valor==i:
                list_palabra_2[count]="_"
                letra_encontrada=True
                break
            else:
                letra_encontrada=False
    
    #print(list_palabra_2)

    for i in list_palabra_2:
        if i!= "_":
            anagrama="No es un anagrama"
            break
        else:
            anagrama="Es un anagrama"
    
    print(anagrama)
        
es_anagrama("amor", "roma")

#Solución 2
def is_anagrama (word_one, word_two):
    if word_one.lower()==word_two.lower():
        return False
    return sorted(word_one.lower())== sorted(word_one.lower())

print(is_anagrama("amor", "roma"))
