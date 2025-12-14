with open("2025/day7/test.txt", "r") as file:
    lines = file.readlines()
res = 0
startPos = []
splitters = []

class Tree:
    def __init__(self, pos, val):
        self.pos = pos
        self.val = val
        self.left = None
        self.right = None
    
    def set_left(self, tree):
        self.left = tree

    def set_right(self, tree):
        self.right = tree

    def traversal(self):
        if self.left == None and self.right == None:
            return self.pos
        elif self.left != None and self.right == None:
                return [[self.left.traversal()], self.pos]
        elif self.left == None and self.right != None:
            return [self.pos, [self.right.traversal()]]
        else:
            return [[self.left.traversal()], self.pos, [self.right.traversal()]]
    
def search(tree, pos):
    if tree.pos == pos:
        return tree
    elif tree.left != None and tree.right == None:
        return search(tree.left, pos)
    elif tree.left == None and tree.right != None:
        return search(tree.right, pos)
    elif tree.left != None and tree.right != None:
        left_search = search(tree.left, pos)
        right_search = search(tree.right, pos)
        return left_search if right_search == None else right_search if not None else None

for i in range(2, len(lines), 2):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            splitters.append([i, j])

splitters_tree = Tree(splitters[0], 0)
print(splitters)

for i in range(len(splitters)):
    tree = search(splitters_tree, splitters[i])
    left = None
    right = None
    finished = False
    j = i + 1
    while (left == None and right == None) and j < len(splitters):
        if (left == None) and (splitters[j][1] == splitters[i][1] - 1):
            left = Tree(splitters[j], 0)
        if (right == None) and (splitters[j][1] == splitters[i][1] + 1):
            left = Tree(splitters[j], 0)
        j += 1
    if left != None:
        tree.set_left(left)
    if right != None:
        tree.set_right(right)
print(splitters_tree.traversal())

for l in lines:
    print(l)
print(res)