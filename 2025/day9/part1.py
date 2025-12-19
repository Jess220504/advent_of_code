with open("2025/day9/doc.txt", "r") as file:
    lines = file.readlines()
points = []

def calculate_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

for i in range(len(lines)):
    point = lines[i][0:-1].split(",")
    points.append([int(point[0]), int(point[1])])
    
max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = calculate_area(points[i], points[j])
        if area > max_area:
            max_area = area
            
print(max_area)