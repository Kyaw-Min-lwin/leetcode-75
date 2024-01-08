class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_search(node):
    stack = [node]
    s = []

    while stack:
        temp = stack.pop()
        s.append(temp.val)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)

    return s


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

result = depth_first_search(a)
print(result)
