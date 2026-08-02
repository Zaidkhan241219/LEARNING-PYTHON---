# File Name :- While_loop.py

# WHILE LOOP QUESTIONS

"""Question 1 (While Loop)
Print all odd numbers from 1 to 25."""

# num=1
# while num<=25:
#     if num%2!=0:
#         print(num)
#     num+=1
    
"""Question 2 (While Loop)
Print the multiplication table of a number entered by the user."""

# num=int(input("Enter The Number : ").strip())
# print(f"The multiplication table of the number {num} : ")
# i=1
# while i<=10:
#     print(f"{num} * {i} = {num*i}")
#     i+=1

"""Question 3 (While Loop)
Reverse a given number. Example Input: 12345 Output: 54321"""

# num=int(input("Enter The Number : ").strip())
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print("Reversed Number = ",reverse)

"""Question 4 (While Loop)
Check whether a number is a Palindrome."""

# String Ke Saath
#num=int(input("Enter The Number : ").strip())
#str1=str(num)
#str2=str1[::-1]
#if str1==str2:
#        print("The Number You Typed Is Pallidrome")
#else :
#        print("Typed Number Is Not A Pallidrome")    

# Int Ke Saath 
# num = int(input("Enter The Number: "))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# if original == reverse:
#     print("The Number You Typed Is Palindrome")
# else:
#     print("The Number You Typed Is Not A Palindrome")

"""Question 5 (While Loop)
Find the sum of digits of a given number.
Example Input: 5829 Output: 24"""

# num = int(input("Enter The Number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num = num // 10
# print("Sum of digits =", sum)

"""Question 6 (While Loop)
Keep asking the user to enter a password until the correct password (python123) is entered."""

# pswd="python123"
# while True :
#     text=str(input("Enter The Password : "))
#     if pswd==text :
#         print("Entered Password Is Correct ")
#         break 
#     else:
#         print("Wrong Password!!! , Try Again")

"""Question 7 (While Loop)
Check whether a given number is a Prime Number."""

# num=int(input("Enter The Number : ").strip())
# if num<=1:
#     print("Invalid Number")
# else:
#     i=2
#     while i<num:
#         if num%i==0:
#             print("Number Is Not Prime")
#             break
#         i+=1
#     else:
#             print("Number Is prime")

"""Question 8 (While)
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

secret_number=39
attempt=0
while True:
    guess=int(input("Guess Your Number : "))
    attempt+=1
    if guess>secret_number:
        print("Too High")
    elif secret_number>guess:
        print("Too Low")
    else:
        print("You Guessed It Correct !!")
        print(f"You Made {attempt} Attempts")
        print("Star Pattern:")
        for j in range(1,attempt+1):
            print("*"*j)
        break