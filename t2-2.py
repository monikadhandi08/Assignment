def menu():
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Division")
    print("[4] Multiplication")
    print("[5] Average")

menu()
x=int(input("Choose any one option which is mentioned above: "))

num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))

if x==1:
    a=num1+num2
    print("Sum of these 2 numbers is:",a)

elif x==2:
    a=num1-num2
    print("Subtraction of these 2 numbers is:",a)

elif x==3:
    a=num1/num2
    print("Division of these 2 numbers is:",a)

elif x==4:
    a=num1+num2
    print("Multiplication of these 2 numbers is:",a)

elif x==5:
    num3=int(input("Enter a number: "))
    num4=int(input("Enter another number: "))
    a=(num1+num2+num3+num4)/4
    print("Average of these numbers is:",a)

if a<0:
    print("Negative")
    