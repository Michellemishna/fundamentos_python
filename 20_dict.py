person = {
    "name": "Nicolas",
    "last_name": "Molina",
    "langs": ["python", "javascript"],
    "age": 99
}
print(person)

#Reemplaza el valor de una key
person["name"] = 'santi'
#se puede modificar un numero de una lista dentro de un diccionario con operaciones matematicas
person["age"] -= 50
#Agrega un valor a una key que es una lista
person['langs'].append('rust')
print(person)

print(person["age"])
person["twitter"] = "@nicobytes"
person["name"] = "Felipe"

#Elimina una key y su valor
del person["last_name"]
person.pop("age")
print(person)
#keys: nos permite obtener las keys del diccionario
print(person.keys())

#values: nos permite obtener los valores del diccionario
print(person.values())

#items: nos permite obtener los items del diccionario key  y valor en forma de tuplas 
print(person.items())

