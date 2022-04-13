print ('veamos si tu numero es par o impar ')
print ('coloca un numero entero')
numero = int (input())
operacion = numero % 2
if operacion == 0:
    print (str(numero) + ' ' + 'es par')
else:
    print (str(numero) + ' ' + 'es impar')