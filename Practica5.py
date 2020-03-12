# el siguiente algoritmo resulve el problema para realizar la suma o multiplicacion  de dos numeros decimales
# dependiendo del valor 
a = 0
b = 0 
c = 0 

a =float(input("ingrese el primer numero" ))
b =float(input("ingrese el segundo numero" ))

if   a > 0  or b >  0 :
  
 print("suma de numeros")
 c = a + b 


else  :
 print ("multiplicacion de numeros")
 c = a*b 

print ("el resultado es : " +str(c))