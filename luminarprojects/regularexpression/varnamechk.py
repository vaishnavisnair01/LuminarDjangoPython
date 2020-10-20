import re
pattern=input("enter the variable")
rule="[a-z][369][a-z0-9]*"
match=re.fullmatch(rule,pattern)
if match==None:
    print("invalid")
else:
    print("valid")