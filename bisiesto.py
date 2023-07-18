
def esYearBisiesto_(fecha):
  # Proposito: indica si el año ingresado por parametro es bisiesto o no.
    
  if esDivisiblePor400_(fecha) or esDivisiblePor4YNo100_(fecha):
    print("es bisiesto")
  else:
    print("no es bisiesto")

def esDivisiblePor400_(fecha):
  # Proposito: indica si el año ingresado por parametro es divisible por 400
  return fecha % 400 == 0

def esDivisiblePor4YNo100_(fecha):
  # Proposito: indica si el año es divisible por 4 y no es divisible por 100
  return esDivisiblePor4_(fecha) and not esDivisiblePor100_(fecha)

def esDivisiblePor4_(fecha):
  # Proposito: indica si la fecha ingresada es divisible por 4
  return fecha % 4 == 0

def esDivisiblePor100_(fecha):
  # Proposito: indica si la fecha dada es divisible por 100
  return fecha % 100 == 0

# creo una variable y le asigno el año que ingresa el usuario y lo convierto a un valor entero.
yearAEvaluar = int(input("ingrese por favor el año a evaluar..."))

#paso por argumento la variable definida anteriormente a la funcion tambien definida anterioremente. 
esYearBisiesto_(yearAEvaluar)


