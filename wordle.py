#Ni idea
palabra_ganadora = 'pollo'
contador = 0
while True:
    adivinanza = input('Ingrese palabra de 5 letras')
    if palabra_ganadora == adivinanza : #Escenario de Acierto
            print('Has acertado')
            break
    else : #Intentos fallidos
    #Funcion de contador, introducir dentro de los intentos fallidos
               contador = contador + 1
    if contador < 6:
        print(f'Te quedan {6-contador} intentos')
    else :
        print('Perdiste')
        break

    
 