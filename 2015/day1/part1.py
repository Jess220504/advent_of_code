with open("2015/day1/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
for i in lines[0]:
    if i == "(":
        res += 1
    elif i == ")":
        res -= 1
print(res)