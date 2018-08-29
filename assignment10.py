#Q.1- Write a Python program to read n lines of a file.

with open('test.txt','r') as f:
    lines=f.readlines()
    n=int(input("Enter the number of lines you want to print"))
    print(lines[:n])

#Q.2- Write a Python program to count the frequency of words in a file.

f=open('test.txt')
data=f.read()
d=data.split()
print(d)
count=0
check=input('Enter the word: ')
for word in d:
    if check==word:
    count=count+1
print(check,count)
f.close()

#Q.3- Write a Python program to copy the contents of a file to another file.

with open('file1.txt') as f:
    print("Data in First File: ",f.read())
    fdata=f.read()
with open('file2.txt', 'r+') as s:
    print('Data in Second File: ',s.read())
    s.write(fdata)
with open('file2.txt') as s:
    print("After copying from First to Second File: ",s.read())

#Q.4- Write a Python program to combine
#     each line from first file with the corresponding line in second file.

with open('test.txt') as f:
    print("The Data from A: ",f.read())
with open('sample.txt') as m:
    print("The Data from B: ",m.read())
with open('test.txt') as f:
    with open('sample.txt','r+') as m:
        a=f.read()
        b=m.read()
        aa=a.split()
        bb=b.split()
        for i in range(len(aa)):
            x=str(aa[i]+bb[i]) + '\n'
            m.write(x)
with open('sample.txt') as m:
    print("The Data from B: ",m.read())

#Q.5- Write a Python program to write 10 random numbers into a file.
#   Read the file and then sort the numbers and then store it to another file.

import random as r
with open('abc.txt','r+') as f:
    for i in range(10):
        x=str(r.randint(1,101)) +'\n'
        f.write(x)
with open('abc.txt') as f:
    print(f.read())
with open('abc.txt','r+') as f:
    with open('result.txt','w') as r:
        data=f.read()  
        d=data.split()
        d.sort()
        r.write(str(d))
with open ('result.txt') as r:
    print(r.read())
    
