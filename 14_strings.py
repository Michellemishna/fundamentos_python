text = "Ella sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
  print("Elegiste bien")
else:
  print("Tambien elegiste bien")
  
#len: nos permite saber cuantos caracteres tiene

size = len(text)
print(size)

#upper: nos permite pasar todo a mayusculas
print(text)
print(text.upper())

#lower: nos permite pasar todo a minus
print(text.lower())

#count: nos permite contar cuantas veces aparece un caracter
print(text.count("a"))

#swapcase: nos permite pasar de mayusculas a minusculas y viceversa
print(text.swapcase())

#startswith: nos permite saber si un texto inicia con algo en especifico
print(text.startswith("Ella"))

#endswith: nos permite saber si un texto termina
print(text.endswith("Rust"))

#replace: nos permite reemplazar una palabra por o
print(text.replace("Python", "R"))


#capitalize: nos permite poner la primera letra en
text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize())

#title: nos permite poner la primera letra de cada palabra en mayus
print(text_2.title())

#isdigit: nos permite saber si un texto es un digito
print(text_2.isdigit())
print("398".isdigit())

