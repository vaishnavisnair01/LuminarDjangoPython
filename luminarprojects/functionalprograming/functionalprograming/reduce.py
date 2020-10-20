from functools import *
lst=[10,11,12,13,14]
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)
max=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(max)