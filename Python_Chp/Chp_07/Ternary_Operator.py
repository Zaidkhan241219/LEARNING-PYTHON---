# File Name :- Ternary_Operator.py

# TERNARY OPERATOR

""" Q. if age greater than or equal to 18 then print adult else minor """

# age = 20 
# status = "Adult" if age >= 18 else "Minor" 
# print(status)

""" Q.Write a program that finds the larger of two numbers using the ternary operator."""

# a=float(input("Enter The First Number : ").strip())
# b=float(input("Enter The Second Number : ").strip())
# bigger_number= f"{a} is largest number.." if a>b else f"{b} is largest number.."
# print(bigger_number)

""" Q. A customer gets a 10% discount if the purchase amount is $500 or more;
otherwise,no discount. Write a program using the ternary operator to calculate the final amount."""
 
# amount=float(input("Enter Your Total Amount ($) : ").strip())
# final_amount=f"Your Final Amount After Discount = {(amount)-(amount*(18/100))}$" if amount>=500 else f"No Valid Discount Your Final Amount = {amount}"
# dicount_value=print(f"Discount Applied = {(amount*(18/100))}")
# print(final_amount)

""" Q. Write a program that assigns a grade using nested ternary operators: 
    Marks ≥ 90 → "A" Marks ≥ 75 → "B" Marks ≥ 50 → "C" Otherwise → "F"""

marks = float(input("Enter Your Marks: "))

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 50
    else "F"
)

print(f"Your Grade is: {grade}")