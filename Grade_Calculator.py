#print("Hello world!!!")

def grade_calc():
    obtained_marks = 0
    total_marks = int(input("How much marks each subject is of = "))
    total_subjects = int(input("Total of how many subjects are there = "))
    for i in range(total_subjects):
        while True:
            marks = float(input(f"Enter marks of subject {i+1}: "))
            if marks > total_marks:
                print("❌ Invalid! Marks cannot be greater than total marks.")
            elif marks < 0:
                print("❌ Invalid! Marks cannot be negative.")
            else:
                obtained_marks += marks
                break
    percentage = (obtained_marks /(total_marks*total_subjects))*100
    print(f"\nTotal Marks Obtained = {obtained_marks}/{total_marks * total_subjects}")
    print(f"Percentage = {percentage:.2f}%")
    if percentage>90 :
        print("You Got Grade A+")
    elif percentage>=75:
        print("You Got Grade A")
    elif percentage>=60:
        print("You Got Grade B")
    elif percentage>=40:
        print("You Got Grade C")
    elif percentage>=35:
        print("You Got Grade D")
    else :
        print("You Got Grade F which means you are FAIL!!!!!")
grade_calc()