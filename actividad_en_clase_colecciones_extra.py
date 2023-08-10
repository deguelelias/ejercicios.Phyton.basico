"""
Consigna
A partir de una lista realizar las siguientes tareas sin modificar la lista original:
Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
Realizar una suma de todos los números que quedan (sum(lista))
Añadir como primer elemento de la lista la suma realizada insert(0, suma)
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
concuerda con el primer número de la lista
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
Nota: Recuerda que para sumar todos los números de una lista puedes usar sum
"""
lista_original = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print("\tLista Original:", lista_original,"\n")

#borro los elementos repetidos en la lista
print ("\tborro los elementos repetidos:")
lista_sin_repeticiones=[]
for numero in lista_original :
    if not numero in lista_sin_repeticiones:
        lista_sin_repeticiones.append(numero)
print(lista_sin_repeticiones)

#ordeno la lista sin los duplicados de mayor a menor
print("\tordeno la lista de mayor a menor")
lista_ordenada=sorted(lista_sin_repeticiones)[::-1]
print(lista_ordenada," \n")

#eliminar los elementos impares de la lista
print("\telimino todos los elementos impares de la lista...\n")
lista_sin_numeros_impares = []
for num in range(-len(lista_ordenada), len(lista_ordenada)):
    if ((lista_ordenada[num] % 2)== 0):
        lista_sin_numeros_impares.append(lista_ordenada[num])
print(lista_sin_numeros_impares)

#realizo la sumatoria de los elementos restantes y lo añado al principio
print("\tcalculando la sumatoria de los elementos restantes...\n")
sumatoria = sum(lista_sin_numeros_impares)
print(sumatoria)
lista_final=[sumatoria]+lista_sin_numeros_impares
print(lista_final)



