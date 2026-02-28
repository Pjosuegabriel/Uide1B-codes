"""dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")"""

# 1. Imprime toda la tupla
"""print("Dias de la Semana:", dias_semana)"""

# 2. Imprime el primer y último elemento de la tupla
"""print("Primer día de la semana:", dias_semana[0])
print("Último día de la semana:", dias_semana[6])
print("Tercer dias de la semana:", dias_semana[2])"""



#Ejercicio en clase

"""lista_frut = ["manzana", "melon", "naranja", "sandia", "uva"]
print("Mis frutas favoritas son:", lista_frut)
print("La fruta que mas me gusta de la lista es:", lista_frut[1])
print("La fruta que menos me gusta de la lista es:", lista_frut[4])

lista_frut.append("cereza") #appende "se usa para agregar un elemento al final de la lista"
print(lista_frut)
lista_frut.remove("uva") #remove "se usa para eliminar un elemento específico de la lista"
print(lista_frut)
lista_frut.insert(0, "fresa") #insert "se usa para insertar un elemento en una posición específica de la lista"
print(lista_frut)
for fruta in lista_frut: #for "se usa para iterar sobre los elementos de una lista o tupla"
    print(fruta)"""

lista_notas = [8.5, 9, 10, 7.5]
print("Mis notas son:", lista_notas)
lista_notas.remove(7.5)
lista_notas.append(9.5)
print("Mis notas actualizadas son:", lista_notas)
lista_notas.insert(3, 8.0)
promedio = sum(lista_notas) / len(lista_notas) #sum se sumar los elementos de una lista" y len "se usa para obtener la cantidad de elementos en una lista"
print("El promedio general de tus notas es:", promedio)
