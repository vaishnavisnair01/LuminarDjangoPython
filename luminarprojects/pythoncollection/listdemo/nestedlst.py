employee=[[1,'ahana',25000],
          [2,'boby',23000],
          [3,'davis',34000],
          [4,'roniya',43000]]
# print name of all employee
for data in employee:
    print(data[1])
# sum of salary of all employee
total=0
for data in employee:
    total=total+data[2]
print(total)
# print name of employee whoes salary>25
for data in employee:
    if(data[2]>=25000):
        print(data[1])