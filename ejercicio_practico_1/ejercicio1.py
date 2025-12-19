
# promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedios = 4
dalto_curso = 1.5
#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000  // otros_cursos_max / 10
diferencia_con_promedios = 100 - dalto_curso / otros_cursos_promedios * 100

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedios * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto /10


#mostrando las diferencia de duracion (ejercicioA)
print(f'El curso de dalton dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de dalton dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de dalton dura un {diferencia_con_promedios}% menos que el mas rapido')

#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempovacio')

#mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedios * 100 // dalto_curso / 10} horas de otros cursos ")