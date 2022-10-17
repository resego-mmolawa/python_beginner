def add(first_value, second_value):
    return first_value + second_value

def subtract(first_value, second_value):
    return first_value - second_value

def multiply(first_value, second_value):
    return first_value * second_value

def divide(first_value, second_value):
    return first_value / second_value

#user inputs
print('Please select the operation.')
print('a. Add')
print('b. Subtract')
print('c. Multiply')
print('d. Divide')

choice = input('Please enter choice (a/b/c/d):')

num_1 = float(input('Please enter the first number:'))
num_2 = float(input('Please enter the second number:'))

if choice == 'a':
    print(num_1, '+', num_2, '=', add(num_1, num_2))

elif choice == 'b':
    print(num_1, '-', num_2, '=', subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, '*', num_2, '=', multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, '/', num_2, '=', divide(num_1, num_2))

else:
    print('This is an invalid input')
