import re
text = "Ten 10, Twenty 20, Thirty 30"
result = re.findall("\d+", text)
for element in result:
    print(element)