text = "Ella sabe Python"
#text = "0123456789112345"
print(text[0])
print(text[1])
#print(text[999])
size = len(text)
print("size => ",size)

print(text[size - 1])
print(text[-1])

#slicing: nos permite sacar ciertas partes del texto
print(text[0:5]) #toma desde el caracter 0 hasta el 5 sin tomar en cuenta el 5
print(text[10:16]) #toma desde el caracter 10 hasta el 16 sin tomar en cuenta el 16
print(text[:10]) #toma desde el caracter 0 hasta el 10 sin tomar en cuenta el 10
print(text[5:-1]) #toma desde el caracter 5 hasta el ultimo caracter
print(text[5:]) #toma desde el caracter 5 hasta el ultimo caracter
print(text[:])
print(text[10:16:1]) #salto de 1 en 1
print(text[10:16:2]) #salto de 2 en 2
print(text[::2]) #va de inicio a fin saltando de 2 en 2

