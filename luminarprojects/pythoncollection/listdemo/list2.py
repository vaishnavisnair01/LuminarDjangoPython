# #print elmts n sum of list
# lst=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in lst:
#     print(i)
#     sum+=i
# print(sum)
# print even no in lst
lst=[2,4,6,8,1,5,7,9,100,101]
sumeven=0
sumodd=0
# for i in lst:
#     if(i%2==0):
#         print(i)
#sum of odd n even no
for i in lst:
    if(i%2==0):
        sumeven+=i
    else:
        sumodd+=i
print("odd sum is",sumodd)
print("even sum is",sumeven)