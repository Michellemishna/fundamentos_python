matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

#para acceder a un elemento de la matriz dentro de otra matriz
print(matriz[0])
print(matriz[0][1])

#para recorrer la matriz entrando en cada una de las listas
for row in matriz:
  print(row)
  for column in row:
    print(column)

