#This code will teach diff. b/w NORMAL PRINT and f-STRING PRINT   5*4*3*2*1

# def factorial() :
#     num = int(input("Enter the number whose factorial you want :"))
#     result =1
#     for i in range(1 , num+1):
#         result*=i
    
#     print(f"Factorial of {num} is {result}...")
    
# factorial()
def factorial() :
    num = int(input("Enter the number whose factorial you want :"))
    result =1
    for i in range(1 , num+1):
        result*=i
    
    print("Factorial of", num , "is = " , result )
    
factorial()
