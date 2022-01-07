# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
'''
l=[1, 4.5, 2, 8, 'add', 2j, 3.6, 'name', 9j, 7]
print(l)'''

# 2. Create a list of size 5 and execute the slicing structure
'''
l=[1, 2, 3, 4, 5]
a=l[1:4]
print(a)'''

# 3. Write a program to get the sum and multiply of all the items in a given list.
'''from functools import reduce
x=reduce(lambda x,y:x+y, [1,2,3,4,5,6])
y=reduce(lambda x,y:x*y, [1,2,3,4,5,6])

print("The sum is:",x)
print("The multiplication is:",y)'''

# 4. Find the largest and smallest number from a given list.
'''
l=[2,1,6,4,8,9,50,3]

l.sort()
print("smallest number is:",l[0])
print("Largest number is:",l[-1])'''

# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
'''
l=[1,2,3,4,5,6,7,8,9]

x=[ x for x in l if x%2!=0]
print(x)'''

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).
''''
x=[x**2 for x in range(1,31) if  x==1 or x>25]

print(x)'''

# 7. Write a program to replace the last element in a list with another list.
'''
l1=[1,3,5,7,9,10]
l2=[2,4,6,8]
l1[-1:]=l2
print(l1)'''

# 8. Create a new dictionary by concatenating the following two dictionaries:

'''a={1:10,2:20}
b={3:30,4:40}
a.update(b)

print(a)'''

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1

'''x={k:k*k for k in range(1,6)}
print(x)'''

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
'''

x=input("Enter a comma separated values:")
list=x.split(",")
tuple=tuple(list)
print("list:",list)
print("tuple:",tuple)'''

