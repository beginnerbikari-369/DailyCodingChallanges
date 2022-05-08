# A unival tree (which stands for "universal value") is a tree where
# all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def unival(root):
    count = 0
    ls = []
    ls.append(root)
    while(ls):
        k = ls.pop(0)
        if k is None:
            continue
        if k.left is None and k.right is None:
            count += 1
        try:
            if k.left.data is k.right.data:
                count += 1
        except AttributeError:
            pass
        ls.append(k.left)
        ls.append(k.right)
    return count


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)
    root.right.left.right.left = Node(1)
    root.right.left.right.right = Node(1)
    # root = Node(10)
    # root.left = Node(20)
    # root.right = Node(30)
    # root.left.left = Node(40)
    # root.right.right = Node(50)
    # root.right.right.left = Node(60)
    # root.right.right.right = Node(70)
    count = unival(root)
    print(count)
