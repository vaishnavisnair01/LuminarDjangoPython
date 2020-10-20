num=int(input("enter the number"))
rem=0
cube=0
number=0
while(num>0):
    rem=num%10
    cube=rem**3
    number=number+cube
    num=num//10
print(number)