with open("Jour3/doc.txt", "r") as file:
    lines = file.readlines()
first_number = 0
index = 0
res = 0

def find_first_number(line):
    r = 0
    index = 0
    for i in range(len(line)):
        if int(line[i]) > r and i < len(line)-1:
            r = int(line[i])
            index = i
    return r, index

for i in range(len(lines)):
    first_number, index = find_first_number(lines[i][:-1])
    second_number = 0
    for j in range(index+1, len(lines[i][:-1])):
        if int(lines[i][j]) > second_number:
            second_number = int(lines[i][j])
    res += first_number*10 + second_number
print(res)