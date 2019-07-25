# Sequential stack  <== 用数组结构实现Stack ==> 顺序栈


class SqStack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = []
        self.top = -1   # -1 means empty stack

    def push(self, value):
        length = self.len()
        if length == self.capacity:
            print("Full stack. No more room")
            return -1

        self.top += 1
        self.list.append(value)

        return 0

    def pop(self):
        length = self.len()

        if length == 0:
            print("Empty stack. No more element")
            return -1

        top_value = self.list.pop(self.top)
        self.top -= 1

        return top_value

    def len(self):
        return self.top + 1

    def traverse(self):
        print ("Data in the stack is {}".format(self.list))

a = SqStack()
a.pop()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
a.traverse()
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
a.traverse()
print(a.pop())
a.pop()



