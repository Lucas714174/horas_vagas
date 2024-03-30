#*************************************List*********************************

#contador
i = 0
lista = []
while i <= 20:
  #print ("par" if i % 2 == 0 else "impar")
  if i % 2 == 0:
    res = "É par"
  else:
    res ="É impar"
  #print([f'{i} {res}'])
  lista.append(i)
  i+=1
print(lista)

#///

for i in lista:
  print ("par" if i % 2 == 0 else "impar")

lista[2] = "oi sumido"
del lista[3]
print(lista)

i=0
while i < len(lista):
  print(lista[i])
  i+=1



