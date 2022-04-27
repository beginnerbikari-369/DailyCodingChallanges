class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = Node(data)

    def traverse(self):
        temp = self.head
        ls = []
        while(temp is not None):
            ls.append(temp.data)
            temp = temp.next
        return ls


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(3)
    l1.insert(7)
    l1.insert(8)
    l1.insert(10)
    ls1 = l1.traverse()
    l2 = LinkedList()
    l2.insert(99)
    l2.insert(1)
    l2.insert(8)
    l2.insert(10)
    ls2 = l2.traverse()
    for i in range(len(ls1)):
        if ls1[i] in ls2:
            print(ls1[i])
            break
