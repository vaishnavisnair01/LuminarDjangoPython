import re
mob=input("enter the no")
rule="(91)?[\d]{10}"
match=re.fullmatch(rule,mob)
if match==None:
    print("invalid")
else:
    print("valid")