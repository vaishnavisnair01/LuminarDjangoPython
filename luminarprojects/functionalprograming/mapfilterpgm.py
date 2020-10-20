
numbers=[1,2,3,4,5]
data=list(map(lambda num:num**2,numbers))
print(data)

evens=list(filter(lambda num:num%2==0,numbers))
print(evens)
namea=["kkr","dc","kxp","mi","csk"]
upp=list(map(lambda data:data.upper(),namea))
print(upp)
from functools import *
num=[10,11,12,13,14]
tot=reduce(lambda num1,num2:num1+num2,num)
print(tot)
