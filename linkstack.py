# Link stack  <== 用链表结构实现Stack ==> 链式栈


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkStack:
    # no need to use head node
    # here top means head pointer
    # here may add one property: count to count for the entire stack
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("Empty stack. No more element")
            return -1

        top_node = self.top
        self.top = self.top.next

        return top_node.data

    def traverse(self):
        datas = []
        p = self.top
        while p:
            datas.append(p.data)
            p = p.next
        print("Data in the stack is {}".format(datas))


link_stack = LinkStack()
link_stack.pop()

n = 20
for i in range(n):
    link_stack.push(i+1)
    link_stack.traverse()

for i in range(n):
    link_stack.pop()
    link_stack.traverse()

link_stack.pop()