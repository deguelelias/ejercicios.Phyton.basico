
def esYearBisiesto_(fecha):
  # indica si el año ingresado por el parametro es bisiesto o no.
  if esDivisiblePor400_(fecha) or esDivisiblePor4YNo100_(fecha):
    print("es bisiesto")
  else:
    print("no es bisiesto")

def esDivisiblePor400_(fecha):
  # indica si el año ingresado por parametro es divisible por 400
  return fecha % 400 == 0

def esDivisiblePor4YNo100_(fecha):
  # indica si el año es divisible por 4 y no es divisible por 100
  return esDivisiblePor4_(fecha) and not esDivisiblePor100_(fecha)

def esDivisiblePor4_(fecha):
  return fecha % 4 == 0

def esDivisiblePor100_(fecha):
  return fecha % 100 == 0


yearAEvaluar = input("ingrese por favor el año a evaluar...")

esYearBisiesto_(yearAEvaluar)


