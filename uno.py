## Variable con elementos del mismo tipo
## lista de numeroes pares

numerospares = []

##generar un ciclo while que de 10 vueltas
## variable centinela
contador = 0
while (contador<10):

    numerospares.append(int (input("Digite un numero par: ")))
    ## append es para llenar
    
    contador=contador+1

for observador in numerospares:
    print(observador)