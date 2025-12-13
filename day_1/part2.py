with open("Day1/doc.txt", "r") as file:
    lines = file.readlines()
num = 50
old_num = num
res = 0

for i in range(len(lines)):
    line = lines[i][:-1]
    rotation = int(line[1:])
    if line[0] == "R":
        while rotation != 0:
            num += 1
            rotation -= 1
            if num == 100:
                num = 0
            if num == 0:
                res += 1
    if line[0] == "L":
        while rotation != 0:
            num -= 1
            rotation -= 1
            if num == -1:
                num = 99
            if num == 0:
                res += 1
    
print(res)