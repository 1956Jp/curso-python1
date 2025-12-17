#DIR: DEVUELBE LA LISTA DE ATRIBUTOS VALIDOS DEL OBJETO PASADO

#UPPER- combierte a mayuscula
#LOWER- convierte a minusculas
#CAPITALIZE- primera en mayuscula

#FIND - metodo encuentra la primera aparicion del valor especificado, sino devuelve1
#INDEX - metodo encuentra la primera aparicion del valor especificado, sino devuelbe una excepcion

#ISNUMERIC - si es numerico devuelbe true

#ISALPHA -se es alfa numerico devuelbe true

#COUNT -devuelbe elnumero de ocurrencia de una sub cadena en la cadena dada
#LEN -cuenta los caracteres de una cadena

#ENDSWITH -verifica si una cadena comienza con
#STARTSWITH -verifica si una cadena termina con

#REPLACE -remplaza u valor por otro
#SPLIT -separa por el parametro dado



cadena1 = "Hola soy Dalton"

cadena2 = "1958"
# Biemvenidos 2 a Yaritagua 1
#print(dir(cadena1))
#print(dir(4))
#print(dir(["soadasoi"]))

#resultado = "Hola mostro como andas".upper()
#resultado = cadena1.lower() 
mayuscula = cadena2.upper()
#resultado = cadena1.capitalize() 
letra_capital = cadena2.capitalize()
#resultado = cadena1.upper() 
#buscar una cadena en otra cadena
busqueda_find = cadena1.find("s")


es_numerico = cadena2.isnumeric()
es_alpha = cadena2.isalpha()
#contamo las coincidencia en una cadena
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena2)
                                   
print(contar_caracteres)


