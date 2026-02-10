print("Bienvenido al identificador de numeros pares e impares. Digite 0 para continuar: ")
a =  int(input())
if (a == 0):
    while (a != 1):

        numeroDigitado = input("Por favor, ingrese un valor: \n")
        mitadNumeroDigitado = int(numeroDigitado)/2
        moduloNumeroDigitado = int(numeroDigitado)%2

        print(f"Numero ingresado: {numeroDigitado}\n")
        print(f"Mitad del numero ingresado: {mitadNumeroDigitado}\n")

        '''Determinar si es par o impar si es par a=1 , si es impar a=0'''
        if (moduloNumeroDigitado == 0):
            a = 1
            print(f"El numero digitado: {numeroDigitado} es par")
        else:
            a = 0
            print(f"El numero digitado: {numeroDigitado} es impar")
else:
    print("Debe digitar 0 para continuar")