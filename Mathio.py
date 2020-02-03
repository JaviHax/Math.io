'''
Codigo desarrollado por Javier "JaviHax" Rivas 2019.
'''

#code starts here
from os import system
from termcolor import colored

def main():
    menu()

def menu():
    system('clear')
    print("\033[1;32;40m ")
    print("  __  __       _   _       _____ ____  ")
    print(" |  \/  |     | | | |     |_   _/ __ \ ")
    print(" | \  / | __ _| |_| |__     | || |  | |")
    print(" | |\/| |/ _` | __| '_ \    | || |  | |")
    print(" | |  | | (_| | |_| | | |_ _| || |__| |")
    print(" |_|  |_|\__,_|\__|_| |_(_)_____\____/ ")
    print(" By JaviHax")
    print("BIENVENIDO AL RESOLUSOR DE ECUACIONES.\nSeleccione un metodo.")
    #b stands for bucket, thats where te variables if the input method are going.
    b = input("1-Gauss.\n2-Gauss-Jordan.\n3-Jacobi.\n4-Gauss-Seidel.\n5-Seidelito (solo matrices 2x3).\n6-Salir.\nSu opcion: ")
    if b == '1':
        Gauss()
    elif b == '2':
        Gauss_Jordan()
    elif b == '3':
        Jacobi()
    elif b == '4':
        Gauss_Seidel()
    elif b == '5':
        Seidelito()
    elif b == '6':
        print("Gracias por usar la calc, vuelva pronto!")
        exit()
    else:
        print("Opcion desconocida.")
        menu()

def Gauss():
    fila_uno = []
    fila_dos = []
    fila_tres = []

    print("Bienvenido al metodo de resolucion por eliminacion Gaussiana.")
    print("ingrese todos los valores de su fila uno y su valor ampliado.")
    for numero in range(4):#filling the first list
        b = input(f"Ingrese valor {numero + 1}: ")
        fila_uno.append(int(b))
    print("ingrese todos los valores de su fila dos y su valor ampliado.")
    for numero in range(4):#filling the second list
        b = input(f"Ingrese valor {numero + 1}: ")
        fila_dos.append(int(b))
    print("ingrese todos los valores de su fila tres y su valor ampliado.")
    for numero in range(4):#filling the third list
        b = input(f"Ingrese valor {numero + 1}: ")
        fila_tres.append(int(b))

    #original matrix
    print("\n\n\nMatriz original.")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #FIRST STEP
    '''
    this part of the code makes the inicial division between the first value
    in the first column to take out the lower values in the same column, in other words
    converts the value in the position 1x1 in the matrix to one.
    [1,x,x]
    [x,x,x]
    [x,x,x]
    '''
    L = fila_uno[0]#u stands for upder in the division
    for i in range(len(fila_uno)):
        U = fila_uno.pop(0)
        insert = U/L#here happens the division
        fila_uno.append(insert)#replacing with the new values
    
    #1st mod matrix
    print("\nMatriz modificada 0.")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #SECOND STEP
    '''
    this converts the value in the position 1x2 of the matrix to zero.
    [1,x,x]
    [0,x,x]
    [x,x,x]
    '''
    b = fila_dos[0]
    if b > 0:#This makes the first validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_dos.pop(0)
            b = aux + auxiliary_array[i]
            fila_dos.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_dos.pop(0)
            b = aux - auxiliary_array[i]
            fila_dos.append(b)

    print("\nMatriz modificada 1.")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    '''
    this part makes an special division for the position 2x2 to convert that number to one.
    [1,x,x]
    [0,1,x]
    [x,x,x]
    '''
    b = fila_dos[1]
    for i in range(len(fila_dos)):
        fila_dos.append(fila_dos.pop(0)/b)

    print("\nMatriz modificada 2")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #THIRD STEP
    '''
    here we convert the first value in the lower of the column 1 to make it zero.
    [1,x,x]
    [0,1,x]
    [0,x,x]
    '''
    b = fila_tres[0]
    if b > 0:#This makes the second validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_tres)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux - auxiliary_array[i]
            fila_tres.append(b)

    print("\nMatriz modificada 3")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #FOURTH STEP
    '''
    this part makes the value in the position 2x1 equal to zero.
    [1,x,x]
    [0,1,x]
    [0,0,x]
    '''
    b = fila_tres[1]
    if b > 0:#This makes the second validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_dos:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_dos)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_dos:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_dos)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    print("\nMatriz modificada 4")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #FIFTH STEP
    '''
    this part of the code makes the special division between the final row and itself to make the last
    value of the last column one.
    [1,x,x]
    [0,1,x]
    [0,0,1]
    '''
    b = fila_tres[2]
    for i in range(len(fila_tres)):
        fila_tres.append(fila_tres.pop(0)/b)
    
    print("\nMatriz modificada 4")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    Z = fila_tres[3]#this is the oficial value of Z
    #this part does the mathematical operations to solve the second degree ec
    if fila_dos[2] > 0:#Ec form: Y - Z = n
        Y = (- fila_dos[2] * Z) + fila_dos[3]
    else:# Ec form: Y + Z = n
        Y = (abs(fila_dos[2]) * Z) + fila_dos[3]

    op1 = fila_uno[1] * Y
    op2 = fila_uno[2] * Z
    
    if op1 > 0 and op2 > 0:# Ec form:  X + Y + Z = n
        X = fila_uno[3] - op1 - op2
    elif op1 < 0 and op2 > 0:#EC form: X - Y + Z = n
        X = fila_uno[3] + abs(op1) - op2
    elif op1 > 0 and op2 < 0:#Ec form: X + Y - Z = n
        X = fila_uno[3] - op1 + abs(op2)
    else:#Ec form: X - Y - Z = n
        X = fila_uno[3] + abs(op1) + abs(op2)

    print(f"\nLos valores encontrados en el sistema por el metodo de Eliminacion Gaussiana son:\nX = {round(X, 2)}\nY = {round(Y, 2)}\nZ = {round(Z, 2)}")
    b = input("1- Volver al menu.\n2- Salir.\nSu decision: ")
    if b == '1':
        menu()
    elif b == '2':
        exit()
    else:
        print("Valor desconocido, regresando al menu.")
        menu()

def Gauss_Jordan():
    fila_uno = []
    fila_dos = []
    fila_tres = []

    print("Bienvenido al metodo de resolucion por Gauss-Jordan.")
    print("ingrese todos los valores de su fila uno y su valor ampliado.")
    for numero in range(4):#filling the first list
        b = input(f"Ingrese valor {numero + 1}: ")
        fila_uno.append(int(b))
    print("ingrese todos los valores de su fila dos y su valor ampliado.")
    for numero in range(4):#filling the second list
        b = input(f"Ingrese valor {numero + 1}: ")
        fila_dos.append(int(b))
    print("ingrese todos los valores de su fila tres y su valor ampliado.")
    for numero in range(4):#filling the third list
        b = input(f"Ingrese valor {numero + 1}: ")
        fila_tres.append(int(b))

    #original matrix
    print("\n\n\nMatriz original.")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #FIRST STEP
    '''
    this part of the code makes the inicial division between the first value
    in the first column to take out the lower values in the same column, in other words
    converts the value in the position 1x1 in the matrix to one.
    [1,x,x]
    [x,x,x]
    [x,x,x]
    '''
    L = fila_uno[0]#u stands for upder in the division
    for i in range(len(fila_uno)):
        U = fila_uno.pop(0)
        insert = U/L#here happens the division
        fila_uno.append(insert)#replacing with the new values
    
    #1st mod matrix
    print("\nMatriz modificada 0.")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #SECOND STEP
    '''
    this converts the value in the position 1x2 of the matrix to zero.
    [1,x,x]
    [0,x,x]
    [x,x,x]
    '''
    b = fila_dos[0]
    if b > 0:#This makes the first validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_dos.pop(0)
            b = aux + auxiliary_array[i]
            fila_dos.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_dos.pop(0)
            b = aux - auxiliary_array[i]
            fila_dos.append(b)

    print("\nMatriz modificada 1.")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    '''
    this part makes an special division for the position 2x2 to convert that number to one.
    [1,x,x]
    [0,1,x]
    [x,x,x]
    '''
    b = fila_dos[1]
    for i in range(len(fila_dos)):
        fila_dos.append(fila_dos.pop(0)/b)

    print("\nMatriz modificada 2")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #THIRD STEP
    '''
    here we convert the first value in the lower of the column 1 to make it zero.
    [1,x,x]
    [0,1,x]
    [0,x,x]
    '''
    b = fila_tres[0]
    if b > 0:#This makes the second validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_tres)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux - auxiliary_array[i]
            fila_tres.append(b)

    print("\nMatriz modificada 3")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #FOURTH STEP
    '''
    this part makes the value in the position 2x1 equal to zero.
    [1,x,x]
    [0,1,x]
    [0,0,x]
    '''
    b = fila_tres[1]
    if b > 0:#This makes the second validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_dos:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_dos)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_dos:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_dos)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    print("\nMatriz modificada 4")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #FIFTH STEP
    '''
    this part of the code makes the special division between the final row and itself to make the last
    value of the last column one.
    [1,x,x]
    [0,1,x]
    [0,0,1]
    '''
    b = fila_tres[2]
    for i in range(len(fila_tres)):
        fila_tres.append(fila_tres.pop(0)/b)
    
    print("\nMatriz modificada 5")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #SIXTH STEP
    '''
    in this step im solving the position 2x3 and changing the value of that position to zero using the
    Gauss-Jordan method.
    [1,x,x|X]
    [0,1,0|Y]
    [0,0,1|Z]
    '''
    b = fila_dos[2]
    if b > 0:
        b *= -1
        for i in fila_tres[2:]:
            aux = i * b
            c = fila_dos.pop(2)
            fila_dos.append(aux + c)

    else:
        b = abs(b)
        for i in fila_tres[2:]:
            aux = i * b
            c = fila_dos.pop(2)
            fila_dos.append(aux + c)


    print("\nMatriz modificada 6")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    #SEVENTH STEP
    '''
    in this step i want to change the value of the position 1x3 to zero.
    [1,x,0|X]
    [0,1,0|Y]
    [0,0,1|Z]
    '''
    b = fila_uno[2]
    if b > 0:
        b *= -1
        auxiliary_array = []
        for i in fila_tres:
            aux = i * b
            auxiliary_array.append(aux)

        for i in range(len(fila_uno[1:])):
            aux = fila_uno.pop(1)
            b = aux + auxiliary_array[i+1]
            fila_uno.append(b)

    else:
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:
            aux = i * b
            auxiliary_array.append(aux)

        for i in range(len(fila_uno)):
            aux = fila_uno.pop(1)
            b = aux + auxiliary_array[i]
            fila_uno.append(b)

    #EIGHT STEP
    '''
    in this step im finishing the last elimination.
    [1,0,0|X]
    [0,1,0|Y]
    [0,0,1|Z]
    '''
    print("\nMatriz modificada 7")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    b = fila_uno[1]
    if b > 0:
        b *= -1
        aux = fila_uno.pop(1)
        c = aux + b
        fila_uno.insert(1, c)
        aux = fila_uno.pop(3)
        c = b * fila_dos[3]
        b = aux + c
        fila_uno.insert(3, b)
    else:
        b = abs(b)
        aux = fila_uno.pop(1)
        c = aux + b
        fila_uno.insert(1, c)
        aux = fila_uno.pop(3)
        c = b * fila_dos[3]
        b = aux + c
        fila_uno.insert(3, b)

    print("\nMatriz modificada Final")
    print(fila_uno)
    print(fila_dos)
    print(fila_tres)

    X = fila_uno[3]
    Y = fila_dos[3]
    Z = fila_tres[3]

    print(f"Los valores encontrados por el metodo de Gauss-Jordan son:\nX = {round(X, 2)}\nY = {round(Y, 2)}\nZ = {round(Z, 2)}")
    b = input("1- Volver al menu.\n2- Salir.\nSu decision: ")
    if b == '1':
        menu()
    elif b == '2':
        exit()
    else:
        print("Valor desconocido, regresando al menu.")
        menu()

def Jacobi():
    print("Bienvenido al metodo de resolucion por Jacobi.")

    n = input("Por favor ingrese su numero de iteraciones a realizar: ")
    A1 = []
    for i in range(3):
        b = input("Ingrese valor de linea A1: ")#here i fill the row one
        A1.append(int(b))
    A2 = []
    for i in range(3):
        b = input("Ingrese valor de linea A2: ")#here i fill the row two
        A2.append(int(b))
    A3 = []
    for i in range(3):
        b = input("Ingrese valor de linea A3: ")#here i fill the row three
        A3.append(int(b))
    B = []
    for i in range(3):
        b = input("Ingrese valor de columna B (los valores se ubicaran de arriba hacia abajo.): ")#here i fill the B column
        B.append(int(b))
    x1,x2,x3 = 0,0,0
    '''
    here i start the iterative loop, i inizialise the values outside the loop because this method requires an starting
    value of zero.
    [^---->]
    [| ^^ |]
    [|loop|]
    [| VV |]
    [<----v]
    '''
    print("\n\nINICIA LA ITERACION\n")
    for i in range(int(n)):
        X1 = (B[0] - (A1[1] * x2) - (A1[2] * x3)) / A1[0]#father
        X2 = (B[1] - (A2[0] * x1) - (A2[2] * x3)) / A2[1]#father
        X3 = (B[2] - (A3[0] * x1) - (A3[1] * x2)) / A3[2]#father
        errorx1 = ((X1 - x1) / X1) * 100#error calculus
        errorx2 = ((X2 - x2) / X2) * 100
        errorx3 = ((X3 - x3) / X3) * 100
        x1 = X1#son
        x2 = X2#son
        x3 = X3#son

        print(f"ITERACION {i + 1}")
        print(f"El valor {i + 1} de X1 es: {round(X1, 3)}")
        print(f"El porcentaje de error para X1 en la iteracion {i + 1} es de: {round(errorx1, 4)}%")
        print(f"El valor {i + 1} de X2 es: {round(X2, 3)}")
        print(f"El porcentaje de error para X2 en la iteracion {i + 1} es de: {round(errorx2, 4)}%")
        print(f"El valor {i + 1} de X3 es: {round(X3, 3)}")
        print(f"El porcentaje de error para X3 en la iteracion {i + 1} es de: {round(errorx3, 4)}%")
        print("\n\n\n")
        
    print("Ejecucion terminada.")
    b = input("1- Volver al menu.\n2- Salir.\nSu decision: ")
    if b == '1':
        menu()
    elif b == '2':
        exit()
    else:
        print("Valor desconocido, regresando al menu.")
        menu()

def Gauss_Seidel():
    print("Bienvenido al metodo de resolucion por Gauss-Seidell.")
    print("Avertencia, este metodo solo resuelve matrices cuyo orden sea el siguiente.")
    print("[@,-,-|X]")
    print("[+,@,+|Y]")
    print("[-,+,@|Z]")
    print("\n")
    print("[@,-,-|X]")
    print("[-,@,-|Y]")
    print("[-,-,@|Z]")
    '''
    Este metodo solo resuelve el caso especifico en el que los valores hayan sido ordenados
    de esa manera, de otro modo hubiese tenido que programar 59/60 plantillas distintas para
    hacer que este proceso tuviese redundancia y fuese aplicable para cualquier matriz, el 
    calculo para determinar cuantos tipos habia que trabajar lo hice de forma manual/grafica.

    En el caso de seidelito si implemente la redundancia dado que en seidelito la maxima cantidad
    de permutaciones posibles era 4, de esa manera programe 4 plantillas diferentes para agregar redundancia.
    '''
    n = input("Por favor ingrese su numero de iteraciones a realizar: ")
    fila_uno = []
    fila_dos = []
    fila_tres = []
    for i in range(4):
        b = input("Ingrese valor de linea 1: ")#here i fill the row one
        fila_uno.append(int(b))
    for i in range(4):
        b = input("Ingrese valor de linea 2: ")#here i fill the row two
        fila_dos.append(int(b))
    for i in range(4):
        b = input("Ingrese valor de linea 3: ")#here i fill the row two
        fila_tres.append(int(b))

    opc = input("Desea inicializar la triada x, y, z?\n1-Si.\n2-No.\nSu decision: ")#here you choose if you want to
    if opc == '1':
        b = input("Introduzca valor para x: ")#value for x
        x = int(b)
        b = input("Introduzca valor para y: ")#value for y
        y = int(b)
        b = input("Introduzca valor para z: ")#value for z
        z = int(b)
    else:
        '''
        if you don't do an inizialisation the values automatically will become zero.
        '''
        x,y,z = 0,0,0

    if fila_uno[1] < 0 and fila_uno[2] < 0 and fila_dos[0] > 0 and fila_dos[2] > 0 and fila_tres[0] < 0 and fila_tres[1] > 0:
        print("\nCOMIENZA LA ITERACION")
        for i in range(int(n)):#here i start the iteration.
            X = (fila_uno[3] + (abs(fila_uno[1]) * y) + (abs(fila_uno[2]) * z)) / fila_uno[0]
            errorx = ((X - x) / X) * 100
            x = X
            Y = (fila_dos[3] - (fila_dos[0] * x) - (fila_dos[2] * z)) / fila_dos[1]
            errory = ((Y - y) / Y) * 100
            y = Y
            Z = (fila_tres[3] + (abs(fila_tres[0]) * x) - (fila_tres[1] * y)) / fila_tres[2]
            errorz = ((Z - z) / Z) * 100
            z = Z

            print(f"ITERACION {i + 1}")
            print(f"El valor {i + 1} de X es: {round(X, 3)}")
            print(f"El porcentaje de error para X en la iteracion {i + 1} es de: {round(errorx, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Y, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errory, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Z, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errorz, 4)}%")
            print("\n\n\n")

    elif fila_uno[1] < 0 and fila_uno[2] < 0 and fila_dos[0] < 0 and fila_dos[2] < 0 and fila_tres[0] < 0 and fila_tres[1] < 0:
        print("\nCOMIENZA LA ITERACION")
        for i in range(int(n)):#here i start the iteration.
            X = (fila_uno[3] + (abs(fila_uno[1]) * y) + (abs(fila_uno[2]) * z)) / fila_uno[0]
            errorx = ((X - x) / X) * 100
            x = X
            Y = (fila_dos[3] + (abs(fila_dos[0]) * x) + (abs(fila_dos[2]) * z)) / fila_dos[1]
            errory = ((Y - y) / Y) * 100
            y = Y
            Z = (fila_tres[3] + (abs(fila_tres[0]) * x) + (abs(fila_tres[1]) * y)) / fila_tres[2]
            errorz = ((Z - z) / Z) * 100
            z = Z

            print(f"ITERACION {i + 1}")
            print(f"El valor {i + 1} de X es: {round(X, 3)}")
            print(f"El porcentaje de error para X en la iteracion {i + 1} es de: {round(errorx, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Y, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errory, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Z, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errorz, 4)}%")
            print("\n\n\n")

    else:
        print("Error 404.")

    b = input("1- Volver al menu.\n2- Salir.\nSu decision: ")
    if b == '1':
        menu()
    elif b == '2':
        exit()
    else:
        print("Valor desconocido, regresando al menu.")
        menu()

def Seidelito():
    print("Bienvenido al metodo de resolucion por Seidelito (matrices 2x3).")
    print("!ADVERTENCIA!")
    print("Si los valores absolutos de los coheficientes de la posicion 1x1 y 2x2 no son superiores")
    print("a la sumatoria de todo lo demas, entonces este metodo no funcionara.")

    fila_uno = []
    fila_dos = []
    n = input("Por favor ingrese su numero de iteraciones a realizar: ")
    for i in range(3):
        b = input("Ingrese valor de linea A1: ")#here i fill the row one
        fila_uno.append(int(b))
    for i in range(3):
        b = input("Ingrese valor de linea A2: ")#here i fill the row two
        fila_dos.append(int(b))
    x, y = 0, 0
    X , Y = 0,0
    if fila_uno[1] < 0 and fila_dos[0] > 0:#case 1
        print("\nCOMIENZA LA ITERACION")
        for i in range(int(n)):

            X = (fila_uno[2] + (abs(fila_uno[1]) * Y)) / fila_uno[0]
            Y = (fila_dos[2] - (fila_dos[0] * X)) / fila_dos[1]
            errorx = ((X - x) / X) * 100
            errory = ((Y - y) / Y) * 100
            x = X
            y = Y

            print(f"ITERACION {i + 1}")
            print(f"El valor {i + 1} de X es: {round(X, 3)}")
            print(f"El porcentaje de error para X en la iteracion {i + 1} es de: {round(errorx, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Y, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errory, 4)}%")
            print("\n\n\n")

    elif fila_uno[1] > 0 and fila_dos[0] < 0:#case 2
        print("\nCOMIENZA LA ITERACION")
        for i in range(int(n)):
            X = (fila_uno[2] - (fila_uno[1] * Y)) / fila_uno[0]
            Y = (fila_dos[2] + (abs(fila_dos[0]) * X)) / fila_dos[1]
            errorx = ((X - x) / X) * 100
            errory = ((Y - y) / Y) * 100
            x = X
            y = Y

            print(f"ITERACION {i + 1}")
            print(f"El valor {i + 1} de X es: {round(X, 3)}")
            print(f"El porcentaje de error para X en la iteracion {i + 1} es de: {round(errorx, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Y, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errory, 4)}%")
            print("\n\n\n")
    
    elif fila_uno[1] > 0 and fila_dos[0] > 0:#case 3
        print("\nCOMIENZA LA ITERACION")
        for i in range(int(n)):
            X = (fila_uno[2] - (fila_uno[1] * Y)) / fila_uno[0]
            Y = (fila_dos[2] - (fila_dos[0] * X)) / fila_dos[1]
            errorx = ((X - x) / X) * 100
            errory = ((Y - y) / Y) * 100
            x = X
            y = Y

            print(f"ITERACION {i + 1}")
            print(f"El valor {i + 1} de X es: {round(X, 3)}")
            print(f"El porcentaje de error para X en la iteracion {i + 1} es de: {round(errorx, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Y, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errory, 4)}%")
            print("\n\n\n")

    else:
        print("\nCOMIENZA LA ITERACION")
        for i in range(int(n)):
            X = (fila_uno[2] + (abs(fila_uno[1]) * y)) / fila_uno[0]
            Y = (fila_dos[2] + (abs(fila_dos[0]) * X)) / fila_dos[1]
            errorx = ((X - x) / X) * 100
            errory = ((Y - y) / Y) * 100
            x = X
            y = Y

            print(f"ITERACION {i + 1}")
            print(f"El valor {i + 1} de X es: {round(X, 3)}")
            print(f"El porcentaje de error para X en la iteracion {i + 1} es de: {round(errorx, 4)}%")
            print(f"El valor {i + 1} de Y es: {round(Y, 3)}")
            print(f"El porcentaje de error para Y en la iteracion {i + 1} es de: {round(errory, 4)}%")
            print("\n\n\n")

    print("Ejecucion terminada.")
    b = input("1- Volver al menu.\n2- Salir.\nSu decision: ")
    if b == '1':
        menu()
    elif b == '2':
        exit()
    else:
        print("Valor desconocido, regresando al menu.")
        menu()

if __name__ == "__main__":
    main()