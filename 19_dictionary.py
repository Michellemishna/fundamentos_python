my_diccionary = {}
print(type(my_diccionary))
my_diccionary = {
  "avion": "bla bla bla",
  "name": "Nicolas",
  "last_name": "Molina Monroy",
  "age": 87
}

print(my_diccionary)
#len nos permite saber cuantos elementos hay en el diccionario
print(len(my_diccionary))

#para acceder a un valor del diccionario se usa la key
print(my_diccionary["age"])
print(my_diccionary["last_name"])

#get: nos permite obtener un valor de una key y si no existe nos devuelve un none
print(my_diccionary.get("age"))
print(my_diccionary.get("unvalor"))

#in: nos permite saber si una key esta dentro del diccionario
print("avion" in my_diccionary)
print("otroqueno" in my_diccionary)

