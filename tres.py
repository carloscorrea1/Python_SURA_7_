## crear un menu de opciones

centinela = 0
print("****Enorate de antioquia")
print("***Menu****")
print("1.Agregar pueblos")
print("2.Mostrar pueblos")
print("3.salir")
pueblos=[]
while(centinela!=3):
    pueblo={}
    centinela = int (input("digite su opcion "))
    if(centinela==1):
        
        pueblo['nombre']=input("ingrese el nombre: ")
        pueblo['distancia']=int(input("ingrese las distancia: "))
        pueblo['habitantes']=int(input("ingrese los habitantes: "))
        pueblos.append(pueblo)
    elif(centinela==2):
        print(pueblos)
    elif(centinela==3):
        print("gracias")
        break     
    else:print("Gracias")       
        
        
    
