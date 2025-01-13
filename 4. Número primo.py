"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_primo(numero):
    for i in range(2,numero):
        mensaje=True
        if numero%i==0:
            return False

    return True

print(is_primo(8))
print(is_primo(9))
print(is_primo(7))
print(is_primo(27))

#Imprime los números primos del 1 al 100
for i in range(1,100):
    if is_primo(i):
        print (i)
    else:
        pass