## menu empanadas inteligentes
## agregar empanadas

#nombre de la empenada
## tres ingredientes
# precio 

centinela=0
print("***Menu****")
print("1.Agregar empanadas")
print("2.Mostrar empanadas")
print("3.Salir")
empanadas=[]
ingrdientes=[]

while(centinela!=3):
    empanada={}
    centinela = int(input("ingrese su opcion: "))
    if(centinela==1):
    empanada ['nombre'] =input("empanadas python")
    ingrdientes.append(input("ingrese el ingrediente 1: "))
    ingrdientes.append(input("ingrese el ingrediente 2: "))
    ingrdientes.append(input("ingrese el ingrediente 3: "))
    empanada['ingredientes']= ingrdientes
    empanadas.append(empanada)
    
         
elif(centinela==2):
        
        print(empanadas)    
        
elif(centinela==3):
        
        print(gracias)
        
        break
    else: print("digite una opcion")      




