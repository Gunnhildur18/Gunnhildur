# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___,

n = int(input("Enter the length of the sequence: "))
i = 1
first = 1
second = 2
third = 3
sum_ = 0

while i <= n:
    i += 1
    print(first)
    first, second, third = second, third, first + second + third