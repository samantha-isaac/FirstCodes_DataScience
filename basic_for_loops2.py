#Tamaño grande - Dada una lista, escribe una función que cambie todos los números positivos de la lista a “big”.
#Ejemplo: biggie_size([-1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores ahora son [-1, "big", "big", -5]
number_list = []
def write_big(num):
    if int(num) >= 0:
        number_list.append("big")
    else:
        number_list.append(num)

print("Enter positive and negative numbers. When you are done write stop")        
while True:
    num = input("Enter number: ")
    if num == 'stop': 
        print(number_list)
        break
    else:
        write_big(num)
        
#Contar positivos - Dada una lista de números, crea una función para reemplazar el último valor con el número de valores positivos.  
#(Ten en cuenta que el 0 no se considera un número positivo).
#Ejemplo: count_positives([-1,1,1,1]) cambia la lista original a[-1,1,1,3] y la devuelve
#Ejemplo: count_positives([1,6,-4,-2,-7,-2]) cambia la lista original a [1,6,-4,-2,-7,2] y la devuelve    
number_list = []
sum = 0
def count_positives():
    length = int(len(number_list))
    number_list[length-1] = sum
        

print("Enter positive and negative numbers. When you are done write stop")        
while True:
    num = input("Enter number: ")
    if num == 'stop':
        count_positives()
        print(number_list)
        break
    else:
        if int(num) > 0 :
            number_list.append(num)
            sum = sum + 1
        else:
            number_list.append(num)
            
#Suma total - Crea una función que tome una lista y devuelva la suma de todos los valores en el arreglo.
#Ejemplo: sum_total([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total([6,3,-2]) debería devolver 7
num_list = []
def resul_sum():
    suma = sum(num_list)
    return suma

print("Enter positive and negative numbers. When you are done write stop")        
while True:
    num = input("Enter number: ")
    if num == 'stop':
        sum_total = resul_sum() 
        print(sum_total)
        break
    else:
        num_list.append(int(num))
        
#Promedio - Crea una función que tome una lista y devuelva el promedio de todos los valores.
#Ejemplo: average([1,2,3,4]) debería devolver 2.5        
promedio_list = []
def obtener_promedio():
    promedio = sum(promedio_list)/len(promedio_list)
    return promedio
    
    
print("Enter positive and negative numbers. When you are done write stop")
while True:
    num = input("Enter number: ")
    if num == 'stop':
        final = obtener_promedio()
        print(final)
        break
    else:
        promedio_list.append(float(num))
        
#Longitud - Crea una función que tome una lista y devuelva la longitud de la lista.
#Ejemplo: length([37,2,1,-9]) debería devolver 4
#Ejemplo: length([]) debería devolver 0
length_list = []
def whats_the_length():
    lenght = len(length_list)
    return(lenght)
    
print("Enter positive and negative numbers. When you are done write stop")
while True:
    num = input("Enter number: ")
    if num == 'stop':
        final = whats_the_length()
        print(final)
        break
    else:
        length_list.append(num)
        
#Mínimo - Crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
#(Opcional) Si la lista está vacía, haz que la función devuelva False.
#Ejemplo: minimum([37,2,1,-9]) debería devolver -9
#(Opcional) Ejemplo: minimum([])  debería devolver False        
min_list = []
def lower_number():
    if len(min_list) == 0:
        return False
    else:
        lower = min(min_list)
        return lower

print("Enter positive and negative numbers. When you are done write stop")
while True:
    num = input("Enter number: ")
    if num == 'stop':
        final = lower_number()
        print(final)
        break
    else:
        min_list.append(num)
        
#Máximo - Crea una función que tome una lista y devuelva el valor máximo en el arreglo. 
#(Opcional) Si la lista está vacía, haz que la función devuelva False.
#Ejemplo: maximum([37,2,1,-9]) debería devolver 37
#(Opcional) Ejemplo: minimum([])  debería devolver False
max_list = []
def obtener_num_max():
    if len(max_list) == 0:
        return False
    else:
        num = max(max_list)
        return num

print("Enter positive and negative numbers. When you are done write stop")
while True:
    num = input("Enter number: ")
    if num == 'stop':
        resultado = obtener_num_max()
        print(resultado)
        #print(max_list)
        break
    else:
        max_list.append(int(num))
        
"""#Lista inversa (opcional) - Crea una función que tome una lista y devuelva esa lista con los valores invertidos.  
#Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list([37,2,1,-9]) debería devolver [-9,1,2,37]
num_inversos_list = []
def invertir_num():
    num = 0
    for x in reversed(num_inversos_list):
        num_inversos_list[num] = x
        if num > len(num_inversos_list):
            break
        else:
            num = num + 1
    
    
print("Enter positive and negative numbers. When you are done write stop")
while True:
    num = input("Enter number: ")
    if num == 'stop':
        invertir_num()
        print(num_inversos_list)
        break
    else:
        num_inversos_list.append(int(num))"""