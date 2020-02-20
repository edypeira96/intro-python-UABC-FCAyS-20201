import  types
#creamos una funcion que nos da el numero de decadas 
def obtenerNumeroDeDecadas(dato):
 
#print("numero de decadas" + dtos[0)
#funcion mejorada 

 if type(dato)  is int:
   #no podemos obtener numero de decadad
   #usando dato[0]
   numerodeaniospordecada = 10
   numerodedecadas =  int(dato / numerodeaniospordecada)
   
  print("numero de decadas " + str (int(numerodedecadas))




#Declaramos una variable para el nombre de Eduardo 
nombre =  "Eduardo"

#En python tenemos manera de identificar tipos+
# en la siguiente linea se identifica  y muestra  el tipo 
print(type(nombre))


anios = 21 
# se comprueba tipo de dato de edad 
print (type(anios))

#pedimos que el usuario nos indique nombre de nuevo su nombre
nuevonombre = input("dame tu nombre!!")
print (type(nuevonombre))
nuevaedad = input("dame tu edad!!")
print (type(nuevaedad))
nuevaedad = int(nuevaedad)



#Mostrando inicial y transformando  cadenas 
print ("hola " + nuevonombre)
print ("tu inicial es "+ nuevonombre[1])
print("tu nombre en mayusculas es : " +  nuevonombre.upper())
obtenerNumeroDeDecadas(nuevaedad)
# utilizar  la funcion  para  decadas pasando la nuevaEdad como parametro 



