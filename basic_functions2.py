#Cuenta regresiva - Crea una función que acepte un número como entrada. 
#Devuelve una lista nueva que cuenta de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento).
#Ejemplo: cuentaregresiva(5) debe devolver la lista: [5,4,3,2,1,0]

print("Enter a number: ")
num = input()
conteo_list = []
for x in range(int(num), -1, -1):
    conteo_list.append(x)
print(conteo_list)

#Print y return -  Crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: : print_and_return([1,2]) debe imprimir 1 y devolver 2

num_list = []
print("Enter first number: ")
num1 = input()
num_list.append(num1)
print("Enter second number: ")
num2 = input()
num_list.append(num2)
#print(num_list)

def print_return(num_list):
    print(num_list[0])
    return num_list[1]

print_return(num_list)

#Primero más longitud - Crea una función que acepte una lista y devuelva la suma del primer valor de la lista, 
#más la longitud de la lista.
#Ejemplo: first_plus_length([1,2,3,4,5])  debe devolver 6 (primer valor): 1 +length: 5)

long_list = []
print("Enter first number: ")
small_num = int(input())
print("Enter second number: ")
large_num = int(input())

def sum(long_list):
    #print(long_list)
    #print(long_list[0])
    #print(len(long_list))
    
    x = long_list[0] + len(long_list)
    return x


for x in range(small_num, large_num+1, 1):
    long_list.append(x)
    
first_length = sum(long_list)
print("The first number plus the length of the list is ", first_length)

#Esta longitud, ese valor - Escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
#La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean, todos, el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

values_list =[]
print("Enter the length: ")
length = int(input())
print("Enter the value: ")
value = int(input())

def length_and_value(length, value):
    
    for x in range(0, length, 1):
        if x < length:
            values_list.append(value)
        else:
            return values_list    
    
length_and_value(length, value)
print(values_list)

