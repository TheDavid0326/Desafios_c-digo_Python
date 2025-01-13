"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
# print(mensaje[::-1])
"""
#Solución 1
mensaje="Hola mundo"

mensaje_reves=""
my_list=[]
largo_lista=len(mensaje)

for i in mensaje:
    my_list.append("_")

print(my_list)

for i in mensaje:
    my_list[largo_lista-1]=i
    largo_lista -=1

print(my_list)

for i in my_list:
    mensaje_reves += i

print(mensaje_reves)

#Solución 2
def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text

print(reverse("Hola mundo"))