#1. Actualizar valores en diccionarios y listas
#Cambiar el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [[5,2,3], [15,8,9]].
#Cambiar el last_name del primer alumno de 'Jordan' a 'Bryant'
#En el sports_directory, cambie 'Messi' por 'Andrés'.
#Cambiar el valor 20 en z a 30.
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.- Cambio 10 en x a 15
x[1][0] = 15
print(x)
#2.- Cambio de 'Jordan' a 'Bryant' en students
students[0]['last_name'] = "Bryant"
print(students)
#3.- Cambio de 'Messi' por 'Andrés' en sports_directory
sports_directory['soccer'][0] = "Andrés"
print(sports_directory)
#4.- Cambio 20 en z a 30
z[0]['y'] = 30
print(z)

#-------------------------------------------------------------------------------------------------------------------#
#2. Iterar a través de una lista de diccionarios
def iterateDictionary(students):
    for x in range(0, len(students), 1):
        print("first_name:", students[x]['first_name'], " - last_name:",students[x]['last_name'])
    
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)

#-------------------------------------------------------------------------------------------------------------------#
#3. Obtener valores de una lista de diccionarios
def iterateDictionary2(key = '', list = ''):
    if key == '' or list == '':
        print("Error")
    else:
        for x in range(0, len(list), 1):
            print(list[x][key])
     
food = [
    {'name_of_food' : 'sushi', 'country_of_food' : 'Japan'},
    {'name_of_food' : 'taco', 'country_of_food' : 'Mexico'},
    {'name_of_food' : 'Bao', 'country_of_food' : 'China'},
    {'name_of_food' : 'paella', 'country_of_food' : 'Spain'}
]

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

animals = [
    {'animal' : 'cat', 'colour' : 'grey', 'age' : 3},
    {'animal' : 'cat', 'colour' : 'white', 'age' : 1},
    {'animal' : 'dog', 'colour' : 'black', 'age' : 12},
    {'animal' : 'cat', 'colour' : 'black', 'age' : 8},
    {'animal' : 'dog', 'colour' : 'gold', 'age' : 6}
]

iterateDictionary2('colour', animals) 
iterateDictionary2('country_of_food', food)
iterateDictionary2('age', animals)
iterateDictionary2('first_name', students)

#-------------------------------------------------------------------------------------------------------------------#
#4. Iterar a través de un diccionario con valores de lista
def printInfo(animals_raza):
    for raza in animals_raza.keys():
        print(len(animals_raza[raza]), raza)
        for x in range(0, len(animals_raza[raza]), 1):
            print(animals_raza[raza][x])

animals_raza = {
    'dogs' : ['golden retriever', 'labrador retriever', 'french bulldog', 'beagle', 
              'german shepherd dog', 'poodle', 'bulldog'],
    'cats' : ['Ragdoll', 'Exotic Shorthair', 'British Shorthair', 'Persian', 
              'Maine Coon', 'Sphynx']
}

printInfo(animals_raza)