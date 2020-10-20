low=int(input("enter the lowe limit"))
upp=int(input("enter the upper limit"))
sumeven=0
sumodd=0
for i in range(low,upp):
    if(i%2==0):
        sumeven=i+sumeven

    else:
        sumodd=i+sumodd
    i=i+1
print("sum of even numbers is",sumeven)
print("sum of odd numbers is",sumodd)
