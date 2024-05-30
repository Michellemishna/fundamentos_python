# if: ejecuta una accion si se cumple una condicion y ejecuta todos los if lo que puede hacer mas pesada su ejecucion
if True:
  print("Deberia ejecutarse")

if False:
  print("Nunca se ejecuta")

'''
pet = input( "¿Cual es tu mascota favorita?")

if pet == 'perro':
  print("Genial tienes buen gusto")

if pet == 'gato':
  print("Espero tengas suerte")
  '''
#else: si no se cumple la condicion entonces se ejecuta el else
'''
stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
  print("El stock es correcto")
else:
  print("El stock es incorrecto")
'''

#elif: se usa para agregar mas condiciones si no se cumple la primera
pet = input( "¿Cual es tu mascota favorita?")

if pet == 'perro':
  print("Genial tienes buen gusto")

elif pet == 'gato':
  print("Espero tengas suerte")
  
elif pet == 'pez':
  print( "Eres lo maximo")

else:
  print("No tienes ninguna mascota interesante")

numero = int(input("Ingresa un numero => "))
if numero % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")


