"""
栈和队列都是线性表，而且是操作受限的线性表，或者说是简化版的线性表
由于线性表有数组和链表这两种存储结构，所以栈和队列都有对应的两种实现

由于数组实现的线性表中，插入和删除都会把后面的数据都移动一遍，而队列的主要操作就是一端插入，一端删除，所以这样的效率会很低.
在数组的尾部插入和删除时间复杂度都是O(1)，不存在数据的移动
但是在数组的头插入和删除的时间复杂度都是O(n)，需要移动后面所有的数据  <== 需要处理的地方
因此第一个改进是：
    引入两个指针，front, rear，分别指向头和尾，头部删除后front直接++，后面的数据不往前移
    尾部是插入，插入后rear++,当然这本身就不涉及数据的移动
第一个方法带来的问题就是front一直++,前面的空间就空出来没法利用，因此引出了第二个改进
第二个改进是：
    循环队列： 在尾部插入的时候，如果发现rear已经到达数组的底部，可以看看front的位置，看看是否可以循环从数组开始位置插入
循环队列的问题就是如何判断队列是否为空

细节：
    front指向的是队头元素，第一个元素
    rear指向的是队尾元素的下一个位置
因此：
    队列为空的条件是front == rear,而不是指只有一个元素
    循环队列队满的判断条件是(rear + 1)%sizeofqueue = front <== 始终会浪费一个元素
    参考：https://time.geekbang.org/column/article/41330
"""


# 顺序循环队列
class CircularSqQueue:
    def __init__(self, capacity=5):
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.list = []

    def enqueue(self, value):
        if (self.rear + 1) % self.capacity == self.front:
            # if queue is full, return error
            print ("Queue is full, return error")
            return -1

        self.list.append(value)
        self.rear = (self.rear + 1) % self.capacity

        return 0

    def dequeue(self):
        if self.front == self.rear:
            # if queue is empty, return error
            print("Queue is empty, return error")
            return None

        value = self.list.pop(0)
        self.front = (self.front + 1) % self.capacity

        return value

    def traverse(self):
        print ("Data in the queue is {}".format(self.list))

    def len(self):
        length = (self.rear - self.front + self.capacity) % self.capacity
        print("Length is {}".format(length))
        return length


my_queue = CircularSqQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.len()
my_queue.traverse()
print(my_queue.dequeue())
my_queue.traverse()
my_queue.len()
print(my_queue.dequeue())
my_queue.traverse()
my_queue.len()
print(my_queue.dequeue())
my_queue.traverse()
my_queue.len()
print(my_queue.dequeue())
my_queue.traverse()
my_queue.len()
print(my_queue.dequeue())
my_queue.traverse()
my_queue.len()