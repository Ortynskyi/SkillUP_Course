#Задание 1
def quote(text, author):
    print(text, f'\n {author:>50}')

quote('"Don\'t compare yourself with anyone in this world...\nif u do so, you are insulting yourself"', "Bill Gates")



#Задание 2
list_num=[]
num_1, num_2 = int(input('Numbers 1 ')), int(input('Numbers 2 '))
                
def even_numbers(num_1, num_2):
    global list_num
        
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
        
    for i in range(num_1 + 1, num_2):
        if i % 2 == 0:
            list_num.append(i)

even_numbers(num_1, num_2)

print(f'All even numbers between the numbers {num_1} and {num_2} :', list_num)



#Задание 3
def square(side, filling, symbol):
    if filling:
        s=symbol
    else:
        s=' '
    
    for i in range(side):
        if i == 0 or i == side - 1:
            for j in range(side):
                print('#', end=' ')
        else:
            print('#',end=' ')
            for j in range(1, side - 1):
                print(s, end=' ')
            print('#',end=' ')
        print()

def filling():
    while True:
        result=input('Fill in the square? (y/n)')
        if result in ('y', 'Y', 'yes', 'Yes'):
            return True
        elif  result in ('n', 'N', 'no', 'No'):
            return False
    
square(int(input('Length sides of the square?: ')), filling(), input('What symbol to fill? '))



#Задание 4
def function_min(*numbers):
    print(f'the minimum number of {len(numbers)} numbers:', min(numbers))

function_min(18, 7, 49, 3, 55)



#Задание 5
num_1, num_2 = int(input('Numbers 1 ')), int(input('Numbers 2 '))
                
def product_of_numbers(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1

    x = num_1
    
    for i in range(num_1, num_2):
        x *= i + 1
    
    print(f'the product of numbers from {num_1} to {num_2} is:', x)


product_of_numbers(num_1, num_2)



#Задание 6
def function_integer(numbers):
    print(f'the number consists of {len(str(numbers))} digits')

function_integer(int(input('enter an integer:')))