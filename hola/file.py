num1 = 42 # variaable declara numero entero
num2 = 2.3 # declaracion de variable
boolean = True # variable de declaracion booloean
string = 'Hello World' 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # declaracion de un registro
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # declaracion de un registro
fruit = ('blueberry', 'strawberry', 'banana') # esto es un arreglo
print(type(fruit)) # imprime una funcion llamada fruit
print(pizza_toppings[1]) # imprime una funcion
pizza_toppings.append('Mushrooms') # tomo un elemento y lo agrego al final de la fila 
print(person['name']) # imprime una funcion
person['name'] = 'George' # imprime una funcion 
person['eye_color'] = 'blue' # imprime una funcion
print(fruit[2]) # imprime una fncion 

if num1 > 45: 
    print("It's greater") # declara una condicional if
else:
    print("It's lower") # declara una condicional else 

if len(string) < 5: # es un condicional
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # bucle for
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): # bucle while
    print(x)
    x += 1

pizza_toppings.pop() # esta funcion elimina el ultimo valor
pizza_toppings.pop(1) # esta funcion elimina los dos ultimos valores 

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # es un procedimiento
    for num in range(10): # es un bucle for 
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # es un procedimiento
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)