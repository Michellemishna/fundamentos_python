name = "Mich"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

#De acuerdo al tipo de dato, podemos transformarlo a otro tipo de dato

#Transformar de int a str
print("Mich" + " Sant")
#Transformar de str a int
print(10 + 20)
#Transformar de int a str
print("Mich" + "30")
#si no tenemos el mismo tipo de dato, no podemos hacer la operacion

#para transformar de un tipo de dato a otro, tenemos que hacerlo de la siguiente manera
age = 30
print("Mi edad es " + str(age))
#otra forma de hacerlo es con la funcion format
print(f"Mi edad es {age}")

#input siempre nos devuelve un str
age = input("Escribe tu edad => ")
print(type(age))
#tenemos que transformarlo a int
age = int(age) + 10
print(f"Tu edad en 10 años sera {age}")


