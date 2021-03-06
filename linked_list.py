"""
ToDo: 单链表反转/链表中环的检测/两个有序链表的合并/删除链表倒数第n个节点/求链表的中间节点
"""


class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList():
    def __init__(self):
        # 头结点与头指针 => 如果存在头结点，那么链表的头指针指向头结点
        # 如果不存在头结点，那么头指针指向第一个结点
        # Using the head Node; the head pointer should point to the head Node
        head_node = Node()
        self.head = head_node

    def traverse(self):
        if not self.head.next:
            # Empty list
            print("Empty list")
            return

        datas = []
        p = self.head.next
        while p:
            datas.append(p.data)
            p = p.next

        print ("Data in the list is {}".format(datas))

    # Here we assume the first node containing data is node_1 (index from 1 instead of 0)
    def insert(self, idx, value):
        if idx <= 0:
            print("Invalid idx")
            return

        # Looking for the (i-1)th Node
        p = self.head
        if not p.next:  # Empty List
            if idx == 1:
                new_node = Node(value)
                p.next = new_node
                return
            else:
                print ("Insert {}th node to an empty list should fail".format(idx))
                return

        # Non-empty list, to find (idx-1)th node
        for i in range(idx-1):
            p = p.next
            if not p:
                print ("There is no so many items in the list")
                return

        new_node = Node(value)
        new_node.next = p.next
        p.next = new_node

    def delete(self, idx):
        if idx <= 0:
            print("Invalid idx")
            return

        p = self.head
        # find (idx-1)th node
        j = 1
        while p and j < idx:
            p = p.next
            j += 1

        if not p:
            print("(idx-1)th node or even previous node is null")
            return

        if not p.next:
            print ("idx_th node is null")
            return

        # begin to delete
        print ("idx_th node data is {}. Deleting it".format(p.next.data))
        p.next = p.next.next

    def get_idx_value(self, idx):
        if idx <= 0:
            print("Invalid index")
            return

        p = self.head
        if not p.next:
            "Empty List"
            return

        for i in range(idx):
            p = p.next
            if not p:
                print("The list is not so long")
                return

        print("idx node data is {}".format(p.data))
        return p.data

    # search the fist index whose value is value
    def search_value(self, value):
        p = self.head
        if not p.next:
            print("Empty list")
            return

        p = p.next
        j = 1
        while p:
            if p.data == value:
                print("{}th node is {}".format(j, value))
                return
            else:
                p = p.next
                j += 1

        print("After searching the whole list, {} not found".format(value))
        return

list1 = SLinkedList()
list1.insert(1, 1)
list1.insert(2, 2)
list1.insert(3, 3)
list1.get_idx_value(4)

list1.traverse()


list1.delete(3)
list1.insert(3, 3)
list1.insert(4, 4)
list1.traverse()

list1.get_idx_value(5)
list1.search_value(0)


