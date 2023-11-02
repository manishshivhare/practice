import re
# print(re.search(r"pp", "aPPle", re.IGNORECASE))
# print(re.search(r"^en","enjoy"))
# print(re.search(r"en$","enjoen"))
# print(re.search(r"[Ll]ion", "lion"))
# print(re.search(r"[ ]", "hello World"))
# print(re.search(r"[Yy]ou|me", "You are good"))
# print(re.findall(r"cat|dog","i love both cat and dog"))
# print(re.search(r"p[a-z]*n", "python programming")) 
# print(re.search(r"a+p+", "pineaapple"))
# print(re.search(r"l?over", "lover"))

# result = (re.search(r"^(\w*), (\w*)$", "I, Love")) # return group tuple
# print(result.groups())

print(re.findall(r"\b[a-zA-Z]{5,6}\b", "hello my name is manish"))

print(re.split("([.?!])", "Develop project plan. Execute business development? campaign!"))

print(re.sub(r"(^[\w .-]*), ([\w .-]*)$", r"\2 \1", "shivhare, manish"))