# Design an algorithm that finds the maximum positive integer input by a user

num_int = int(input('Input a number: '))

max_int = 0

while num_int >= 0:
    num_int = int(input('Input a number: '))
    if num_int > max_int:
        max_int = num_int

print('The maxinum is', max_int)