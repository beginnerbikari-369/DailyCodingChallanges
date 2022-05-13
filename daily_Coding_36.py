# Given the root to a binary search tree,
# find the second largest node in the tree.
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(root):
    ans = []
    if root is None:
        return
    Q = Queue()
    Q.put(root)
    while(not Q.empty()):
        node = Q.get()
        if node is None:
            continue
        ans.append(node.val)
        Q.put(node.left)
        Q.put(node.right)
    return ans


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.right.right = Node(50)
    root.right.right.left = Node(60)
    root.right.right.right = Node(70)
    ls = serialize(root)
    ls.sort()
    print(ls)
    # ls.pop(len(ls)-1)
    print(ls[len(ls)-2])
