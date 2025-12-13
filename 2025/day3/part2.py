with open("2025/day3/doc.txt", "r") as file:
    lines = file.readlines()
res = 0

def find_nums(line, n):
    nums = []
    num_skipped = 0
    index = 0
    for i in range(n):
        num = 0
        last_index = index
        for j in range(index, len(line) - n + i + 1):
            if int(line[j]) > num:
                last_index = j
                num_skipped += 1
                num = int(line[j])
        index = last_index + 1
        nums.append(num)
        num_skipped -= 1
    return nums

for i in range(len(lines)):
    line = find_nums(lines[i][:-1], 12)
    line_res = 0
    for j in range(len(line)):
        line_res *= 10
        line_res += line[j]
    res += line_res
    
print(res)