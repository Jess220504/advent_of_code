with open("day6/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
new_tab = []

for line in lines:
    new_line = []
    splitted_line = line.split(" ")
    for i in range(len(splitted_line)):
        if splitted_line[i] != "" and splitted_line[i] != "\n":
            if "\n" in splitted_line[i]:
                new_line.append(splitted_line[i][:-1])
            else:
                new_line.append(splitted_line[i])
    new_tab.append(new_line)

for i in range(len(new_tab[0])):
    col_res = int(new_tab[0][i])
    if new_tab[-1][i] == "*":
        for j in range(1, len(new_tab) - 1):
            col_res *= int(new_tab[j][i])
    else:
        for j in range(1, len(new_tab) - 1):
            col_res += int(new_tab[j][i])
    res += col_res
print(res)