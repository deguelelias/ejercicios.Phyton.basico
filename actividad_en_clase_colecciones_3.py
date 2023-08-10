"""
Descripción de la actividad. 

Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}. 
Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. 
En el caso de ingresar una divisa no existente en nuestro diccionario, deberemos indicarle con 
un mensaje de notificación que la divisa no se encuentra disponible. 

"""
moneda = {'Dolar':'$','Euro':'€', 'Libra':'£'}

divisa_a_visualizar = input("\tpor favor ingrese la divisa que desea ver:...\n")
if(divisa_a_visualizar in moneda):
    print("la divisa seleccionada es:", moneda[divisa_a_visualizar])
else:
    print(f'La divisa {divisa_a_visualizar} no esta disponible')

