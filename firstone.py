#! /usr/bin/python

numberInput = input("Enter a number:")
number_string = str(numberInput)

dig = [int(d) for d in str(number_string)]

print "lenght:", len(dig)
if len(dig) == 1:
  print "One digit number:",dig[0]
  exit()


output = []
pointer=1;
numberToCompare = dig[0]
numList = [];
output.append(dig[0])

while pointer < len(dig):
 print "Index:", pointer
 num = dig[pointer]
 numList[:] = []
 numList.append(dig[pointer]) 
 print "numToCompare:", numberToCompare
 while num < numberToCompare:
       pointer+=1
       if pointer >=  len(dig):
          break
       numList.append(dig[pointer]) 
       num = int(''.join(map(str,numList)))
       #output.append(num)
       print "Number:",num
 pointer+=1
 if num > numberToCompare:
   output.append(num)
 numberToCompare = num;
print output
