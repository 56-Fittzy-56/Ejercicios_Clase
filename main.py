
import random


dia_semana = (input("Qué dia de la semana vas a comprar?: \n"))

if dia_semana == "Miercoles":
    print("pagas 4€")
else:
    age = int(input("Enter your age: \n").lower())
    estudiante = input("Eres un estudiante?: \n")

if age <= 12:
    print("Pagas 4€")

elif estudiante == "si":
     print("pagas un 30% menos")

elif age >= 65:
    print("Pagas 5€")
