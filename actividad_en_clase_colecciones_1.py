"""
Ejercicio:
gordon lanzó su curva&strawberry ha fallado por un pie! 
-gritó Joe Castiglione&dos pies -le corrigió 
Troop&strawberry menea la cabeza como disgustado… 
-agrega el comentarista

tiene que quedar...

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.
"""
# asigno a variables las partes del texto a trabajar.
oracion_1 = "gordon lanzó su curva&strawberry ha fallado por un pie! "
oracion_2 = "-gritó Joe Castiglione&dos pies -le corrigió "
oracion_3 = "Troop&strawberry menea la cabeza como disgustado…"
oracion_4 = "-agrega el comentarista"

#divido las oraciones para poder operar con sus partes
oracion_1 = oracion_1.split("&")
oracion_2 = oracion_2.split("&")
oracion_3 = oracion_3.split("&")

#imprimo dando formato a las variables y modificando mediante las funciones como se muestra el texto en consola
print(f"{(oracion_1[0]).capitalize()}..." )
print(f"- {(oracion_1[1]).capitalize()} {oracion_2[0]} ")
print(f"- {oracion_2[1].capitalize()} {oracion_3[0]}")
print(f"- {oracion_3[1] } {oracion_4}.")


