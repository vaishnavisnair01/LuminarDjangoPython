student={"rollno":1,"name":"vishnu","total":100}
print(student)
print(student["name"])
print("college" in student)
student["college"]="luminar technolab"
print(student)
student["total"]+=100
print(student)
for k in student:
    # print(k)
    print(k,",",student[k])