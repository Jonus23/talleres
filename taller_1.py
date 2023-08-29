
import os
os.system('cls')

'''
1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas
. Luego muestre la lista por consola mediante un ciclo.
'''
materias = list()

r = int(input('cuantas materias desea añadir: '))
print()

for i in range(r):
    clase = input('por favor escriba la materia junto con la nota  ejemplo-[mate: 4.0]:  ')
    materias.append(clase)
    print()

for i in materias:
    print(i)

os.system('pause')

'''
2. Escriba un programa que almacene personas (input), luego que le muestre 
por pantalla el mensaje de ‘Su nombre es ‘nombre’
'''
os.system('cls')

people = list()
personas = int(input('cuantas personas desea añadir: '))
print()

for i in range(personas):
    name = input('nombre de la persona: ')
    people.append(name)
    print()
    
for x in people:
    print(f'Su nombre es {x}')

os.system('pause')

'''
3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.
'''
os.system('cls')

valores = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

euro = 5000
dolar= 4000
yen= 3000


print('pasar de pesos a...')
print('1. euro')
print('2. dolar')
print('3. yen')
print()

pasar= float(input('pesos colobianos que desea pasar: '))
divis= int(input('elija la divisa: '))

if divis == 1:
    res= pasar / euro
    print(valores['Euro'], res)
elif divis == 2:
    res = pasar / dolar
    print(valores['Dollar'], res)
elif divis == 3:
    res = pasar / yen
    print(valores['Yen'], res)
    
os.system('pause')


'''
4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.
'''
os.system('cls')

tupla = [23, 3.4, 'hola']
print (tupla)
n = True

while n == True:
    x = input('Desea agrgar otro valor a la tupla? si o no:   ')
    print()
    lista = list(tupla)
    
    if x == 'si':
        
        print('que tipo de tupla desea:')
        print('1. str')
        print('2. int')
        print('3. float')
        print()
        n1 = int(input('escriba el valor para la operación: '))
        print()
        
        if n1 == 1:
            add = input('escriba el str que desea añadir: ')
            lista.append(add)
            tupla2 = tuple(lista)
            print()

        elif n1 == 2:
            add = int(input('escriba el int que desea añadir: '))
            lista.append(add)
            tupla2 = tuple(lista)
            print()

        elif n1 == 3:
            add = float(input('escriba el float que desea añadir: '))
            lista.append(add)
            tupla2 = tuple(lista)
            print()
        
        else:
            print('ERROR!')
    
    elif x == 'no':
        tupla2 = tuple(lista)
        print('Entendido...')
        print()
        print(tupla2)
        print(type(tupla2))
        n = False
        