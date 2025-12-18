
# promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedios = 4
dalto_curso = 1.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso // otros_cursos_max * 100
diferencia_con_promedios = 100 - dalto_curso / otros_cursos_promedios * 100

print(f'El curso de dalton dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de dalton dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de dalton dura un {diferencia_con_promedios}% menos que el mas rapido')