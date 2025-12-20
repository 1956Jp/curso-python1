import string
import random

longitud = int(input("Ingrese el tamano de la contra sena: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print("La contrasena generada es: " + contrasena)