# File Name :- list_comprehension.py

numbers = [1,2,3,4,5,6,7,8,9]
squares = [number**2 for number in numbers]
print(squares)
even = [number for number in numbers if number%2==0]
print(even)