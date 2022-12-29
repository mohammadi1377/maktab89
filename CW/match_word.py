import re
words = ["Python PHP", "Java JavaScript", "c c++ ","p"]
for w in words:
	m = re.findall("(P\w+)\W(P\w+)", w)
	if m:
	    print(m)