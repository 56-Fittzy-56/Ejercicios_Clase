edad = int(input("Edad: "))
dia = (input("Dia de la semana: "))
dia = dia.lower()
estudiante = input("Eres estudiante si o no: ")
estudiante = estudiante.lower()
precio = 8
if dia == "Miercoles":
    precio = 4
    print("Precio de la semana Miercoles: ", precio)
elif estudiante == "si":
    precio = precio * 0.3
    print("Precio de la semana Si: ", precio)
else:
    if edad <= 12:
        precio = precio / 2
        print("Precio de la semana Miercoles: ", precio)
    elif edad > 12 and edad < 65:
        print("Precio de la semana Miercoles: ", precio)
    else:
        precio = 5
        print("Precio de la semana Si: ", precio)






























