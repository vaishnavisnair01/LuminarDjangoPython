string="ababababbbbabbbb"
import re
pattern="ab"
matcher=re.finditer(pattern,string)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("no of ab",count)