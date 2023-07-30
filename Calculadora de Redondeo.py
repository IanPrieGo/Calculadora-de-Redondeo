
# Introducccion
print('Calculadora de Redondeo')
print('Ingresa un número para redondearlo')

# Definición de Valores
num_float= float(input())  # "float" se refiere a que es un numero decimal
num_resta= int(num_float)
num_decimal= num_float - num_resta  # la diferencia entre "num_float" y "num_decimal" es que el primero es un numero entero acompañado de un decimal (1.9), y el segundo solo tiene el decimal (0.9)

# Comparacion de Valores
if num_float == num_resta:
    print(str(num_resta) + ' ya esta redondeado, buen trabajo!')
elif num_decimal < 0.5:
    print (str(num_float) + ' redondeado, es ' + str(num_resta) + '!')
else:
    print(str(num_float) + ' redondeado, es ' + str(num_resta + 1) + '!')
