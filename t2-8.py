x=input("Enter the string: ")

count1=0
count2=0

for i in x:
    if i.isdigit():
        count1=count1+1
    elif i.isalpha():
        count2=count2+1
print("The number of digit is:")
print(count1)

print("The number of alphabet is:")
print(count2)

