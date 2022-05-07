# Given a singly linked list and an integer k,
# remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def traverse(root):
    temp = root
    while(temp):
        print(temp.data)
        temp = temp.next


def removekth(root, index, len):
    index = len - index + 1
    i = 1
    temp = root
    # print(temp.data)
    while(i != index):
        prev = temp
        temp = temp.next
        # print(temp.data)
        i += 1
    prev.next = temp.next
    return root


if __name__ == "__main__":
    root = Node(10)
    root.next = Node(20)
    root.next.next = Node(30)
    root.next.next.next = Node(40)
    root.next.next.next.next = Node(50)
    # print("new",root.next.next.data)
    newroot = removekth(root, 1, 5)
    traverse(newroot)
