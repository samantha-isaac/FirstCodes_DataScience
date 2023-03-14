import random

def randInt(min = 0, max = 100):
    if min >= max or max <= min :
        return ("Error")
    else:
        if min == 0 and max == 100:
            num = random.random()*100
            return int(num)
        elif min == 0:
            num = random.random()*max + min
            return int(num)
        elif max == 100:
            max = max - min
            num = random.random()*max + min
            return int(num)
        else:
            max = max - min
            num = random.random()*max + min
            return int(num)
    
        

print(randInt())	# debe imprimir un número entero aleatorio entre 0 y 100
print(randInt(max=50)) 	# debe imprimir un número entero aleatorio entre 0 y 50
print(randInt(min=50)) 	# debe imprimir un número entero aleatorio entre 50 y 100
print(randInt(min=50, max=500))    # debe imprimir un número entero aleatorio entre 50 y 500

