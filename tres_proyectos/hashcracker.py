import hashlib

hash_file = "655e786674d9d3e77bc05ed1de37b4b6bc89f788829f9f3c679e7687b410c89b"

dic_file = input("Ingrese la direccion del archivo del diccionario: ")

with open(dic_file, 'r') as file:
    
    diccionario =  [line.strip() for line in file]
    
    
    for password in diccionario:
        
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        
        if hash_calculado == hash_file:
            
            print("La contrasena original es: " + password)
            break
        
        else:
            print("La contrasena no se encuentra en el diccionario") 