#Ciclos While
x = 5
while x > 0:
    print(x)
    x = x-1
print(x)

#Ciclos For
for i in [5,4,3,2,1]:
    print(i)

amigos = ["Richard", "Ariel", "Peter", "Angel"]

for amigo in amigos:
    print("Feliz año nuevo:", amigo)

#Encontrar el numero mas grande en una lista
mayorNumero = None
print("Antes", mayorNumero)
for numero in [3, 41, 12, 7, 69, 4, 15]:
    if mayorNumero is None:
        mayorNumero = numero
    elif numero > mayorNumero:
        mayorNumero = numero
    print(mayorNumero, numero)
print("Despues", mayorNumero)
