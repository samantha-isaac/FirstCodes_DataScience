#Básico - Imprime todos los enteros de 0 a 150. Pista: usa un bucle for y rango.
for x in range(0, 151, 1):
    print(x)


#Múltiplos de cinco - Imprime todos los múltiplos de 5 entre 5 y 1,000
for x in range(0, 1005, 5):
    print(x)


#Contar al estilo Dojo
#Imprime los enteros de 1 a 100. Si el entero es divisible por 5, imprime “Coding” en su lugar. 
#Si es divisible por 10, imprime "Coding Dojo".
for x in range(1, 100, 1):
    if (x % 10) == 0:
        print("Coding Dojo")
    elif (x % 5) == 0:
        print("Coding")
    else:
        print(x) 
 
 
#Whoa. Es un gran idiota - Agrega los enteros impares del 0 al 500,000, e imprime la suma final.
sum = 0
for x in range (0, 500000, 1):
    if (x % 2) != 0 :
        #print(sum)
        sum = x + sum
    else:
        continue
print("La suma total es:", sum)


#Cuenta regresiva de 4 en 4 - Imprime números positivos comenzando desde el 2018, en cuanta regresiva de 4 en 4.
for x in range (2018, 0, -4):
    print(x)
  
    
#Contador flexible (opcional) - Establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum hasta highNum, imprime solo los enteros que sean múltiplos de mult. 
#Por ejemplo, si lowNum=2, highNum=9, y mult=3, el bucle debería imprimir 3, 6, 9 (en líneas sucesivas).   
lowNum = 25
highNum = 264
mult = 4
for x in range(lowNum, highNum+1, 1):
    if (x % mult) == 0:
        print(x)