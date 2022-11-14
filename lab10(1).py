import re

x = open("story.txt", "r")
z=x.read()
result = len(re.findall(r'\w+', z))
M = {}
for key in z.split():
    M[key] = M.setdefault(key, 0) +1
m = open("words.txt", "w")
m.write(str(result))
m.write(" ")
m.write(str(len(M)))
m.write(" ")
m.write(str(len([i for i in z.split('. ')])))
x.close()
