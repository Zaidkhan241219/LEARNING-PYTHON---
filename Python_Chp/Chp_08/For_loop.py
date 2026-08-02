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
# # fact = 1
# if num == 0 or num == 1:
#     print(f"Factorial of {num} is = 1")
# else:
#     for i in range(1, num + 1):
#         fact *= i
# #     print(f"Factorial of {num} is = {fact}")

"""Question 5 (For Loop)
Print the following pattern:
*
**
***
****
***** """ 

# for i in range(1,6):
#     for j in range(1,6):
#         if i==j:
#            print("*"*i)

"""Question 6 (For Loop)
Print the Fibonacci series for the first N terms.
Example
Input: 7
Output:  0  1  1  2  3  5  8 """

# print("ENTER THE NUMBER TILL THE FIBONACCI SERIES YOU WANT")
# num=int(input("Enter The Number Of Terms : ").strip())
# a , b = 0 , 1
# for i in range(num) :
#     print(a , end="  ")
#     c=a+b
#     a=b
#     b=c

"""Question 7 (For Loop)
Check whether a given number is a Prime Number."""

# num=int(input("Enter The Number : ").strip())

# if num<=1:
#     print("Invalid Number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("Number Is Not Prime")
#             break
#         else:
#             print("Number Is prime")

"""Question 8 (For)
Create a Number Guessing Game.
Rules:
Secret number = 27
Keep asking the user to guess until they get it right.
Print "Too High" or "Too Low" after each wrong guess.
Count the total number of attempts.
After the correct guess, print a star pattern where the number of stars equals the number of attempts.
Example
Guess: 15
Too Low
Guess: 40
Too High
Guess: 27
Correct!
Attempts: 3"""

# secret_number=39
# attempt=0
# for i in range(1,100):
#     guess=int(input("Guess Your Number : "))
#     attempt+=1
#     if guess>secret_number:
#         print("Too High")
#     elif secret_number>guess:
#         print("Too Low")
#     else:
#         print("You Guessed It Correct !!")
#         print(f"You Made {attempt} Attempts")
#         print("Star Pattern:")
#         for j in range(1,attempt+1):
#             print("*"*j)
#         break

