#1-----------------------------------------------#
"""def a(): 
    return 5  #sólo devuelve un 5
print(a()) #llama a la función 'a' sin la necesidad de mandar un argumento
#Predicción: 5

#2-----------------------------------------------#
def a():
    return 5 #sólo devuelve un 5
print(a()+a()) #llama dos veces la función 'a' sumándo ambos
#Predicción: 10

#3-----------------------------------------------#
def a():
    return 5   #va a devolver sólamente el 5
    return 10  #ya que el segundo return no es alcanzable ni continuo (?)
print(a())
#Predicción: 5 

#4-----------------------------------------------#
def a():
    return 5  #sucede lo mismo que en el ejercicio 4 ya que por el orden en el que 
    print(10) #ambas lineas se encuentran, nunca va a alcanzar la segunda línea
print(a())
#Predicción: 5

#5-----------------------------------------------#
def a():
    print(5) #la función llama a que "imprima" el número 5
x = a() # la función es llamada y el resultado se le asigna a x
print(x) #imprime x
#Predicción:
#5
#5  -> me equivoqué, pero fue porque literalmente no devuelve nada la función, sólo imprime 5

#6-----------------------------------------------#
def a(b,c):
    print(b+c) #la función no devuelve nada, sólo manda a "imprimir" la suma de ambos valores 
print(a(1,2) + a(2,3))
#Predicción: 
#3
#none
#5
#none -> si imprimió los dos números en ese orden, pero dio error al intentar hacer  la suma por el resultado "none"

#7-----------------------------------------------#
def a(b,c):
    return str(b)+str(c) #pide devolver dos números pero los convierte en string y al haber una suma, va a imprimir ambos números
print(a(2,5))
#Predicción: 25 

#8-----------------------------------------------#
def a():
    b = 100 #se le asigna un valor a un parámetro
    print(b) #se imprime "b"
    if b < 10:    #se hace una comparativa donde no aplica por lo que salta al "else"
        return 5
    else:
        return 10  #devuelve el número 10
    return 7  #nunca va a entrar a este return ya que en la condicionante ambos devuelven un valor
print(a())
#Predicción: 
#100
#10 

#9-----------------------------------------------#
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3  #nunca entra en este return
print(a(2,3))  #b = 2 y c = 3 entra en la comparativa, por lo que devuelve 7
print(a(5,3))  #b = 5 y c = 3 no entra en la comparativa, por lo que devuelve 14
print(a(2,3) + a(5,3)) #hace la suma de ambos valores 7 y 14
#Predicción:
#7
#14
#21 

#10----------------------------------------------#
def a(b,c):
    return b+c 
    return 10  #nunca va a entrar a este return por el orden del código
print(a(3,5)) # b=3 y c=5 por lo que va a devolver la suma de ambos números
#Predicción: 8 

#11----------------------------------------------#
b = 500
print(b) #imprime el valor de 'b'
def a(): 
    b = 300 #cambia el valor de 'b' a 300
    print(b) #imprime el nuevo valor
print(b) #imprime el valor de 'b' de 500
a() #luego ya llama a la función donde se hace el cambio
print(b)
#Predicción:
#500
#500
#300
#300  -> Aquí me equivoqué, ya que se toma este cambio sólo para la función, no se refleja el cambio en el exterior

#12----------------------------------------------#
b = 500
print(b) #imprime primero el valor de 'b'
def a():
    b = 300
    print(b) #imprime el nuevo valor de 'b'
    return b #devuelve el nuevo valor de 'b' pero al no pedir que se imprima o se asigne, no hace nada como tal ni cambia
print(b)
a()
print(b) #no cambia el valor de 'b' por lo que sigue siendo 500
#Predicción:
#500
#500
#300
#500

#13----------------------------------------------#
b = 500
print(b) #imprime el valor de 'b'
def a():
    b = 300
    print(b) #se le asigna nuevo valor a 'b'
    return b #se devuelve ese nuevo valor de 'b'
print(b)
b=a() #se le asigna el valor de 300 dentro de la función al var 'b' externo
print(b) #imprime el nuevo valor de 'b'
#Predicción:
#500
#500
#300
#300

#14----------------------------------------------#
def a():
    print(1)
    b() #llama a la función 'b'
    print(2)
def b():
    print(3) 
a() #primero entra a la función 'a'
#Predicción:
# 1
# 3
# 2 """

#15----------------------------------------------#
def a():
    print(1) #[2] imprime el número 1
    x = b() #[3] se llama a la función 'b' para asignarle valor a 'x' = 5
    print(x) #[6] debería de imprimir el número 5
    return 10 #[7] regrea el número 10
def b():
    print(3) #[4] imprime 3
    return 5 #[5] regresa número 5
y = a() # [1] primero para asignarle valor a 'y' se llama a la función 'a' = 10
print(y) #[8] imprime el valor de 10
#Predicción:
#1
#3
#5
#10

