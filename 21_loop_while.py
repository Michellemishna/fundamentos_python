'''while True:
  print("Se ejecuto")
  '''
#while mientras se cumpla una condicion se ejecuta
counter = 0

while counter < 10:
  counter += 1
  print(f"v1 => {counter}")

#break: nos permite romper el ciclo, no continua con el ciclo
counter2 = 0
while counter2 < 20:
  counter2 += 1
  if counter2 == 15:
    break
  print(f"v2 =>  {counter2}")

#continue: nos permite saltar el ciclo y seguir con el siguiente ciclo
counter3 = 0
while counter3 < 20:
  counter3 += 1
  if counter3 < 15:
    continue
  print(f"v3 => + {counter3}")


