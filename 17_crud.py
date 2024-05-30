#CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

#append: nos permite agregar un nuevo elemento al final de la lista
numbers.append(700)
print(numbers)

#insert: nos permite agregar un nuevo elemento en una posicion especifica
numbers.insert(0, "hola")
print(numbers)
numbers.insert(3, "change")
print(numbers)

#extend: nos permite agregar varios elementos a la lista
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

#index: nos permite saber en que posicion esta un elemento
index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

#remove: nos permite eliminar un elemento de la lista
new_list.remove("todo 1")
print(new_list)

#pop: nos permite eliminar un elemento de la lista y tambien nos permite saber cual elemento fue eliminado
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

#reverse: nos permite invertir el orden de la lista
new_list.reverse()
print(new_list)

#sort: nos permite ordenar la lista de menor a mayor
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)

#sort no funciona con listas que tienen tipos de datos mezclados
new_list.sort()