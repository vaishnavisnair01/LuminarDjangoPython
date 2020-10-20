import re
vehicle=input("enter the no")
rule="kl[\d]{2}[a-z]{1,2}[\d]{4}"
match=re.fullmatch(rule,vehicle)
if match==None:
    print("invalid")
else:
    print("valid")