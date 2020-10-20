# lst=[1,2,3]
# lst2=[4,5,6]

# nlst=[(i,j) for i in lst for j in lst2]
# print(nlst)
# sq=[i*i for i in lst]
# print(sq)
# even=[i for i in lst if i%2==0]
# print(even)
lst=[1,2,3,4,5,6]
# res=list(map(lambda num:num**2,lst))
res=[num**2 for num in lst]
print(res)
