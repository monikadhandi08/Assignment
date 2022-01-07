#  1. Write a program to reverse a string
'''s="1234abcd"
print(s[::-1])'''

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
#Sample input: “abcSdefPghijQkl”
#Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

'''def func(s):
    case={'upper':0,'lower':0}
    for i in s:
        if i.isupper():
            case['upper']=case['upper']+1
        
        if i.islower():
            case['lower']=case['lower']+1
    
    print('original:',s)
    print('upper:',case['upper'])
    print('lower:',case['lower'])

func("abcSdefPghijQkl")'''

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
'''
def func(l):
    return set(list(l))

l=[10,20,30,30,20,40,50,50,60,70]

print(func(l))'''

#  4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words 
# in a hyphen-separated sequence after sorting them alphabetically.
'''
x=input("Enter hyphen-separated sequence of words: ").split('-')
y=[i for i in x]
y.sort()
print('-'.join(y))'''

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making allcharacters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
'''x="Hello world Practice makes man perfect"
i=x.upper()
print(i)'''

# 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
'''
def func(x,y):
    print(x+y)

func('8','9')'''

# 7. Define a function that can accept two strings as input and print the string with the maximum length in the consol.
# If two strings have the same length, then the function should print both the strings line by line.
'''
x,y=input("Enter two strings:").split(",")
def func(x,y):
    if (len(x)>len(y)):
        print("The max. length string is",x)
    elif (len(x)==len(y)):
        print("Both the string have same length")
        print(x)
        print(y)
    else:
        print("The max. length string is",y)

func(x,y)'''

# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
'''
y=map(lambda x:x**2,(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
print(tuple(y))'''

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.
#Sample input: show Numbers(3) (where limit=3)
'''
def showNumbers(limit):
    for i in limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")

showNumbers(3)'''

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
'''
a=filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(list(a))'''

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].
#Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
#numbers in the filtered list. Use lambda() to define anonymous functions.
''''
a=filter(lambda x:x%2==0, [1,2,3,4,5,6,7,8,9,10])
x=list(a)
print(x)

b=map(lambda y:y**2,x)
print(list(b))
'''
# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
'''
def func():
    try:
        5/0
    except ZeroDivisionError:
        print("There was an zero division error")

func()
'''

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
'''
from functools import reduce

x=reduce(lambda x,y:x+y, ['1','2','3','4','5','6','7'])
print(x)
'''

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.
'''
a=filter(lambda x:x%7==0, [7,14,15,21,28,32,35,40,42])
x=list(a)
print(x)

b=filter(lambda x:x%3!=0, x)
print(list(b))'''

# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function 
#to map() to complete the operation.
'''
def multiply(x):
    return x*x

a=map(multiply,[1,2,3,4,5,6])
print(list(a))'''

# 16.  

'''def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)'''

'''def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()'''










