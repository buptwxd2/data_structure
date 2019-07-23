class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList():
    def __init__(self):
        # 头结点与头指针 => 如果存在头结点，那么链表的头指针指向头结点
        # 如果不存在头结点，那么头指针指向第一个结点
        self.head = None  # here we assume no head Node; Otherwise the head should point to head Node

    def traverse(self):
        if not self.head:
            # Empty list
            print("Empty list")
            return

        p = self.head
        while p:
            print("Current node data is {}".format(p.data))
            p = p.next

list1 = SLinkedList()




node2 = Node(2)
list1.head.next = node2

list1.traverse()


