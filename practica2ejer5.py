

'''
1: ingresar números
2: ordenar números
3: calcular el máximo
4: calcular el mínimo
5: calcular el promedio
0: para terminar
'''
lisNumero=[]

while True:
    print('1: ingresar números \n2: ordenar números \n3: calcular el máximo \n4: calcular el mínimo \n5: calcular el promedio \n 0: para terminar')
    opcion = input('Ingrese una opcion: ')
    #me aseguro que ingrese un valor numerico
    while True:
        if not opcion.isdecimal():
            opcion = input('ERROR! ingree un numero: ')
        else:
            opcion = int(opcion)
            break
    #chequeo la opcion y la ejecuto

    if opcion == 1:
        numero = input('Ingree un numero: ')
        while True:
            if not numero.isdecimal():
                numero = input('ERROR! ingree un numero: ')
            else:
                lisNumero.append(int(numero))
                break
        print('Numero ingresado correctamente...\n')
    elif opcion == 2 :
        if not lisNumero:
            print(' Disculpe la lista  esta vacia, utilice opcion uno:\n')
        else:
            print(' se procedera a ordenar la lista\n')
            lisNumero.sort()
    elif opcion == 3 :
        if not lisNumero:
            print(' Disculpe la lista  esta vacia, utilice opcion uno:\n')
        else:
            print('el maximo de la lista es' , max(lisNumero) , '\n')
    elif opcion == 4 :
        if not lisNumero:
            print(' Disculpe la lista  esta vacia, utilice opcion uno:\n')
        else:
            print('el minimo de la lista es' , min(lisNumero) , '\n')
    elif opcion == 5 :
        if not lisNumero:
            print(' Disculpe la lista  esta vacia, utilice opcion uno:\n')
        else:
            promedio = sum(lisNumero)/len(lisNumero)
            print('el promedio es  de la lista es ', promedio, '\n')
    #calcular promedio
    elif opcion == 0 :
        break
    else:
        print('OPCION INCORRECTA...\n')

        Make
        sure
        it
      