# menu empanadas inteligentes
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


while(centinela!=3):
    empanada={}
    ingrdientes=[]
    centinela = int(input("ingrese su opcion: "))
    if(centinela==1):
        empanada['nombre'] =input("ingrese el nombre: ")
        for i in range (3):
            ingrdientes.append(input(f"ingrese el ingrediente :{i+1}"))
        
        empanada['ingredientes']= ingrdientes
        empanada['precio']=int (input("ingrese el precio"))
        
        empanadas.append(empanada)
    
         
    elif(centinela==2):
        
        print(empanadas)    
        
    elif(centinela==3):
        
        print(gracias)
        
        break
    else: print("digite una opcion")      



