class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.val


def breadth_first_search(node):
    queue = [node]
    s = []

    while queue:
        temp = queue.pop()
        s.append(temp.val)
        if temp.left:
            queue.insert(0, temp.left)
        if temp.right:
            queue.insert(0, temp.right)
        print(queue)

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

result = breadth_first_search(a)
print(result)
