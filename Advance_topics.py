#Q.1- Write a python program to print the cube of each value of a list using list comprehension.
lst=[1,2,3,4,5]
i=[i**3 for i in lst]
print("The list is:",lst)
print("Cube of each value of the list:",i)


#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
r= int(input("Enter the range"))
x=[p for p in range(2,r) if 0 not in [p%d for d in range(2,p)]]
print("Prime number in the range are:",x)



#Q.3- Write the main differences between List Comprehension and Generator Expression.
"""In list comprehension, we use parenthesis instead of square brackets and it takes less memory."""


#LAMBDA & MAP


#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius=[39.2, 36.5, 37.3, 37.8]
m=list(map(lambda x:(x * 1.8) + 32,Celsius))
print("Celcius:",Celsius)
print("Fahrenheit: ",m)


#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
l=[1,2,3,4,5]
x = list(map(lambda x:x**2,l))
print("List:",l)
print("Square of all the elements in the list:",x)


#FILTER & REDUCE


#Q.1- Filter out all the primes from a list."""
n=[1,2,3,4,5,6,7,8,9]
for i in n: 
     number=list(filter(lambda x: x == i or x % i and x > 1, n))
print("prime numbers:",number)


#Q.2- Write a python program to multiply all the elements of a list using reduce.
from functools import reduce
l=[1,2,3,4,5]
r=reduce(lambda x, y: x*y,l)
print("Product of all the elements of the list is:",r)
