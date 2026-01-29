# #Ni idea
# palabra_ganadora = 'pollo'
# contador = 0
# while True:
#     adivinanza = input('Ingrese palabra de 5 letras')
#     if palabra_ganadora == adivinanza : #Escenario de Acierto
#             print('Has acertado')
#             break
#     elif
#     else : #Intentos fallidos
#     #Funcion de contador, introducir dentro de los intentos fallidos
#                contador = contador + 1
#     if contador < 6:
#         print(f'Te quedan {6-contador} intentos')
#     else :
#         print('Perdiste')
#         break

#Trabajando en la comparacion de input con la palabra ganadora.
adivinanza = input('Palabra de 5 letras')
intentos = list(adivinanza)
palabra_ganadora = 'pollo'
lista_ganadora = list(palabra_ganadora)
print(lista_ganadora)

for letras in range(5):
    if intentos[letras] == lista_ganadora:
        print(f'Tiene {letra}')

