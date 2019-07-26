"""
链式队列
    1.此处rear指向的不是队尾的后一个位置，就是队尾
    2.front的话分情况，若无head node,则指向第一个node.LinkQueueV1;若有head node,则指向head node，就是LinkQueueV2
    3.在LinkQueueV1里，
        rear == front有两种场景，一个是队为空，一个是队里只含有一个元素
        正常入队操作只需操作rear,但是当队为空时，需要同时更新front
        正常出队操作只需要操作front，但是当队里只有一个元素时，需要同时更新rear
    4.在LinkQueueV2里，
        rear == front只有一种场景，就是队为空，都指向head node.front不变，始终指向head node
        正常入队操作只需操作rear,但是当队为空时，需要同时更新front <== 这个就不需要了
        正常出队操作只需要操作front，但是当队里只有一个元素时，需要同时更新rear  <== 这个还是需要

"""

class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


class LinkQueueV1:
    def __init__(self):
        self.front = None   # here no head Node needed
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        # empty list or one element
        if self.front == self.rear:
            if not self.rear:
                # empty queue
                self.front = new_node
                self.rear = new_node
                return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        # empty list or one element
        if self.front == self.rear:
            if not self.front:
                print("Empty queue. Error")
                return -1
            else:
                # one element
                current_front = self.front
                self.front = self.front.next
                self.rear = None
                return current_front.data

        current_front = self.front
        self.front = self.front.next

        return current_front.data

    def traverse(self):
        data_to_print = []
        p = self.front
        while p:
            data_to_print.append(p.data)
            p = p.next

        print ("Data in the queue is {}".format(data_to_print))


# Another version with head Node
class LinkQueueV2:
    def __init__(self):
        self.front = Node()   # front point to the head node
        self.rear = self.front  # empty queue

    def enqueue(self, value):
        new_node = Node(value)

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front == self.rear:
            print("Empty queue. Error")
            return

        current_front = self.front.next
        self.front.next = self.front.next.next
        # only one element -> reset rear
        if self.rear == current_front:
            self.rear = self.front

        return current_front.data

    def traverse(self):
        data_to_print = []
        p = self.front.next
        while p:
            data_to_print.append(p.data)
            p = p.next

        print ("Data in the queue is {}".format(data_to_print))

# Test V1
my_queue = LinkQueueV1()
my_queue.enqueue(1)
my_queue.traverse()
my_queue.enqueue(2)
my_queue.traverse()
my_queue.enqueue(3)
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()

# Test V1
my_queue = LinkQueueV2()
my_queue.enqueue(1)
my_queue.traverse()
my_queue.enqueue(2)
my_queue.traverse()
my_queue.enqueue(3)
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()
my_queue.dequeue()
my_queue.traverse()