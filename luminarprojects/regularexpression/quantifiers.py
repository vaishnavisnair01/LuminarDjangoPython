import re
pattern="aaaaaabbbaaabbaa"
# x="a+"
# x="a*"
# x="a?"
# x="^a"#given pattern
# x="a$"
# x="a{2}"
x="a{2,3}"
matcher=re.finditer(x,pattern)
for match in matcher:
    print(match.start())
    print(match.group())