# File Name :- For_loop.py

# FOR LOOP QUESTIONS

"""Question 1 (For Loop)
Print numbers from 1 to 20."""

# for i in range(1,21):
#     print(i)

"""Question 2 (For Loop)
Find the sum of numbers from 1 to N."""

# num = int(input("Enter the number till which you want the sum: ").strip())
# total = 0
# for i in range(1, num + 1):
#     total += i
# print(f"SUM FROM RANGE 1 TO {num} IS = {total}")

"""Question 3 (For Loop)
Print all numbers between 1 and 100 that are divisible by 3 and 5."""

# for i in range(1,101):
#      if i%3==0 and i%5 ==0:
#         print(i)

"""Question 4 (For Loop)
Find the factorial of a given number.
Example Input: 5 Output: 120"""

# num = int(input("Enter The Number: "))

# fact = 1

# if num == 0 or num == 1:
#     print(f"Factorial of {num} is = 1")
# else:
#     for i in range(1, num + 1):
#         fact *= i

#     print(f"Factorial of {num} is = {fact}")
    
"""Question 5 (For Loop)
Print the following pattern:
*
**
***
****
*****
""" 

for i in range(1,6):
    for j in range(1,6):
        if i==j:
           print("*"*i)