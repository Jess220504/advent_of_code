with open("2015/day1/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
i = 0
while res != -1:
    if lines[0][i] == "(":
        res += 1
    elif lines[0][i] == ")":
        res -= 1
    i += 1
    print(lines[0][i])
print(i)