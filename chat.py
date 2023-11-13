
dicc = {}

menu= """
1) Registrar Usuario
2) Iniciar Seccion
3) Salir

"""

primero=0
while primero!=3:
    print(menu)
    primero= int(input("Que opcion desea elegir?: "))
    if primero==1:
        usuario=input("Ingrese el usuario: ")
        contraseña=input('Escriba su contraseña: ')
        contraseña2=input('Vuelva a escribir su contraseña: ')
        while contraseña!=contraseña2:
            contraseña2=input('Lo siento su contraseña no coincide, vuelva a escribirla: ')
        dicc[usuario]=contraseña2
    elif primero==2:
        usuario=input('Escriba su usuario: ')
        contraseña=input('Escriba su contraseña: ')
        if dicc.get(usuario)==contraseña:
            print(f'Bienvenido {usuario}')
            primero=3
        else:
            print('Los siento el Usuario o contraseña no son correctos')
    elif primero==3:
        break
    else:
        print('Ingrese una opción válida')


    