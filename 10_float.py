x = 3.3
print(x)

y = 1.1 + 2.2
print(y)
print(x == y) #false

#Comparacion con strings
y_str = format(y, ".2g")
print(y_str)

print(y_str == str(x)) #true

#Comparacion con matematica
print(x, y)
tolerance = 0.00001
 #estoy diciendo que la diferencia entre x y y sea menor a la tolerancia
print(abs(x - y) < tolerance)
