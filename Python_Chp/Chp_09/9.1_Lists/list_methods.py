# File Name :- list_methods.py

numbers=[100 , 300 , 700 , 10000 , 33.44 , 55.6457 , 99 , 2 , 45]

numbers.append(900000)
numbers.sort()
numbers.extend(["hello i am a number" , "keep quite"])
numbers.insert(2 , "now i am at 2nd position")
numbers.remove(700)
numbers.pop(5)
numbers.count(300)
numbers.index(45)
numbers.clear()
print(numbers)
