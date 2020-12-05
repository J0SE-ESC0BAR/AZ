
###While --- mientras
num = 10

while num>0:
    num -=1
    if num ==4:
        print("variable es: ?")
        continue
    print("variable es: "+str(num))

###For --- para
#variable = entrada de texto ("mensaje")
name = input('¿ingresa un nombre?')

counter = 0

#para (una variable) en (otra variable)
for x in name:
    counter +=1        #Contador de letras      x son letas recorridas por for en (variable)
    print("Caracter es #:"+str(counter)+" y la letra es:"+str(x))
else:
    print("El for a terminado de recorrer el nombre")



#...
r = ""
p = True
while p != False:
    name1 = input('¿Ingresa un nombre?')
    counter1=0
    for y in name1:
        counter1 +=1        
        print("#"+str(counter1)+"-"+str(y))

        print("¿Deseas ingresar otro nombre?")
        r = input('-----¿si o no?-----')    
        

        if r == str("si"):
            p = True
        elif r == str("no" or p == False):
            p = False
            print("::::::::::::::::::::::")
            print("::::::::::::::::::::::")
            print(":::Fin del programa:::")
            print("::::::::::::::::::::::")
            print("::::::::::::::::::::::")
        elif r != str("si" or "no"):
            print("introdusca si o no")
