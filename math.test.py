n1 = float(input("Primer numero: ") )
n2 = float(input("Segundo Numero: ") )

opcion = 0
while True:
    print("""
    Elegir opcion
    
    1) Sumar
    2) Restar 
    3) Multiplicar 
    4) Dividir
    5) Salir
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO:",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO:",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO:",n1*n2)
    elif opcion == 4:
        print(" ")
        print("RESULTADO:",n1/n2)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")