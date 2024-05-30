name = "Mich"
last_name = "Sant"
print(name)
print(last_name)

#concaenar
full_name = name + " " + last_name
print(full_name)

quote = "I'am Mich"
print(quote)

quote2 = "She said 'Hello'"
print(quote2)

#format
template = "1 Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "2 Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"3 Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)