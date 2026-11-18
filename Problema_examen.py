#1 pedir al usuario cuantas temperaturas
#2 pedir las x temperaturas al usuario              """ fgsdgfsf """ docstring
#3 hacer la media de las temperaturas e imprimir
from traceback import print_tb

lista = []
numero_temperatura = int(input("Ingrese el numero de temperaturas: "))
for i in range(numero_temperatura):
    nueva_temp= float(input(f"Ingrese el nuevo temperatura: {i+1}"))
    lista.append(nueva_temp)

total = 0
for temperatura in lista:
    total += temperatura
    media = total / numero_temperatura
    print(media)





