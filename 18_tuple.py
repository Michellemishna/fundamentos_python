numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi" , "nico")
print(numbers)
print(type(numbers))

print("0 =>", numbers[0])
print("-1 =>", numbers[-1])

print(strings)  
print(type(strings))

#CRUD
#en las tuplas no se puede agregar o eliminar elementos
#numbers.append(10)
print(numbers)
#tampoco se puede modificar
#numbers[1] = "change"

#metodos de las tuplas
print(strings)
#INDEX: nos permite saber en que posicion esta un elemento
print(strings.index("zule"))

#COUNT cuantos elementos hay del mismo elemento
print(strings.count("nico"))

#LIST para convertir una tupla en una lista
my_list = list(strings)

print(my_list)
print(type(my_list))

my_list[1] = "juli"
print(my_list)

#TUPLE para convertir una lista en una tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
