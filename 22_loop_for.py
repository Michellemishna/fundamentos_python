#el bucle for nos permite recorrer los elementos de una lista o una tupla o un diccionario
#comienza de 0 hasta el ultimo elemento indicado pero el ultimo elemento no se incluye
for element in range(20):
  print(element)

for element in range(1, 21):
  print(element)

#el bucle for nos permite recorrer los elementos de una lista
my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

#el bucle for nos permite recorrer los elementos de una tupla
my_tuple = ("nico", "juli", "santi")
for element in my_tuple:
  print(element)

#el bucle for nos permite recorrer los elementos de un diccionario
product = {
  "name": "camisa",
  "price": 100,
  "stock": 89
}
for key in product:
  print(key, "=>", product[key])

#con items podemos obtener los valores de las keys y los valores en forma de tuplas
for key, value in product.items():
  print(key, "=>", value)

#el bucle for nos permite recorrer los elementos de una lista de diccionarios

people = [
  {
    "name": "nico",
    "age": 34
  },
  {
    "name": "zule",
    "age": 45
  },
  {
    "name": "santi",
    "age": 4
  }
]

for person in people:
  print("name =>", person["name"])
