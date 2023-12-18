import math

a = 3 + 4
b = 3 - 4
c = 3 * 4
d = 3 % 4
e = 3 / 4
f = 3 ** 4
g = 3 // 4

i = [a,b,c,d,e,f,g]
for j in i:
    print(j)

name = "Fuad Sani Ibrahim"
family_name = 'Sani Ibrahim'
country = 'Nigeria'
py = 'I am enjoying 30 days of Python'

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Fuad'))
print(type('Sani Ibrahim'))
print(type('Nigeria'))


integer = 42

float = 3.14

complex = 2 + 3j

string = "Helloworld!"

boolean = True

list = [1, 2, 3, 4, 5]

tuple = (10, 20, 30, 40, 50)

set = {1, 2, 3, 4, 5}

dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}



print("Integer:", integer)
print("Float:", float)
print("Complex:", complex)
print("String:", string)
print("Boolean:", boolean)
print("List:", list)
print("Tuple:", tuple)
print("Set:", set)
print("Dictionary:", dictionary)




x1, y1 = 2, 3
x2, y2 = 10, 8


distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print("Euclidean distance:", distance)