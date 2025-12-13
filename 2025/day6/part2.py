with open("day6/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
tab = []
new_tab = []
final_tab = []

for i in range(len(lines[0]) - 1):
    cpt = 0
    l = ""
    for j in range(len(lines)):
        if lines[j][i] == " ":
            cpt += 1
        else:
            l += lines[j][i]
    tab.append(l)

for i in range(len(tab)):
    new_tab.append(tab[i])
    if tab[i] == "":
        final_tab.append(new_tab[:-1])
        new_tab = []

final_tab.append(new_tab)
for i in range(len(final_tab)):
    col_res = int(final_tab[i][0][:-1])
    if final_tab[i][0][-1] == "*":
        for j in range(1, len(final_tab[i])):
            col_res *= int(final_tab[i][j])
    else:
        for j in range(1, len(final_tab[i])):
            col_res += int(final_tab[i][j])
    res += col_res
    
print(res)