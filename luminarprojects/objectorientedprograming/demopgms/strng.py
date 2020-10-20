# str="HEY"
# res=""
# cnt=0
# for i in str:
#     cnt+=1
#     res+=i*cnt
# print(res)
lst=[1,2,3,4,5,6,7]
# res=list(map(lambda num:num-1 if num<5 else num+1,lst))
res=[x-1 if x<5 else x+1 if x>5 else x for x in lst]
print(res)