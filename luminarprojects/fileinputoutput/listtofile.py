ref=open("number","r")
lst=[]
for numbers in ref:
    print(numbers)
    numbers=int(numbers.rstrip())
    lst.append(numbers)
print(lst)
sum=sum(lst)
print(sum)
max=max(lst)
print(max)
min=min(lst)
print(min)