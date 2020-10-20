import re
# x="[abc]" chk for a,b or c
# x="[a-z]"
# x="[1-9]"
# x="[A-Z]"
# x="[a-zA-Z]"
# x="[a-zA-Z0-9]"#IT WILL CHK FOR ALL WORDS
# x="[^a-zA-Z0-9]"
# x="[^0-9]"
#predefinrd characters
# x="\s"#chk for spaces
# x="\d"#chk for digit==[0-9]
# x="\D"#==[^0-9]
# x="\w"#==[a-zA-Z0-9]
x="\W"#==[^a-zA-Z0-9]
matcher=re.finditer(x,"ab7 c@KZ")
for match in matcher:
    print(match.start())
    print(match.group())

