# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deserialize(ls):
    for i in range(len(ls)):
        if ls[i] is not None:
            ls[i] = Node(ls[i])
        root = ls[0]
    i = 0
    while(i < len(ls)):
        if ls[i] == "":
            i += 1
            continue
        if ls[i] is None:
            ls.insert(2*i+1, "")
            ls.insert(2*i+2, "")
        if ls[i] is not None:
            try:
                ls[i].left = ls[2*i + 1]
            except IndexError:
                ls[i].left = None
            try:
                ls[i].right = ls[2*i + 2]
            except IndexError:
                ls[i].right = None
        i += 1
    return root

# def Inorder(root,ls):
#     if root:
#         ls.append(root.val)
#         Inorder(root.left, ls)
#         Inorder(root.right, ls)
#     else:
#         ls.append(None)
#     return ls


def serialize(root):
    ans = []
    if root is None:
        return
    Q = Queue()
    Q.put(root)
    while(not Q.empty()):
        node = Q.get()
        if node is None:
            ans.append(None)
            continue
        ans.append(node.val)
        Q.put(node.left)
        Q.put(node.right)
    return ans

# def serialize(root):
#     ls = [root]
#     newls = []
#     i = 0
#     while(ls):
#         print(newls[i])
#         if ls[i] is not None:
#             newls.append(ls[i].val)
#         else:
#             newls.append(None)
#         i += 1
#         node = ls.pop(0)
#         if node.left is not None:
#             ls.append(node.left.)
#     return newls


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.right.right = Node(50)
    root.right.right.left = Node(60)
    root.right.right.right = Node(70)
    ls = serialize(root)
    print(ls)
    root = deserialize(ls)
    ls = serialize(root)
    print(ls)
