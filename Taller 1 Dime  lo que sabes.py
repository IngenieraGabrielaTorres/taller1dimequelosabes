#Taller 1
#Dime lo que sabes 
#Gariela Torres
#ID:1001970935
#ID:502193
#correo:gabriela.torresr@correo.upb.edu.co
#Cel:3234708201
#Diplomado de PYTHON APLICADO A LA INGENIERIA 
 

#Defino las variables de mi ecuacion
def ecuacion1(a,b,c,d,e,f):
#Defino y retorno a mi ecuacion
    return ((a+(b/c))/(d+(e/f)))
#asigno valores a mis variables
ecu1 = ecuacion1(100,200,300,400,500,600)
#imprimo 
print("ecu1",ecu1)

#Defino las variables de mi ecuacion
def ecuacion2(a,b,c,d):
#Defino y retorno a mi ecuacion
    return (a-(b/(c-d)))
#asigno valores a mis variables
ecu2 = ecuacion2(100,200,300,400)
#imprimo 
print("ecu2",ecu2)

#cambio de variables
ecu1,ecu2 = ecu2,ecu1

#imprimo
print(ecu1)
print(ecu2)