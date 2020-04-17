# heap structure and heap operations: insert and pop
# here since heap is a complete tree, we are using an array to store/represent a tree


# suppose this is a max heap(not min heap)
class my_heap():
    def __init__(self, ini_list):
        self.my_list = ini_list[:]      # use an array to store the heap/tree elements;
        self.my_list.insert(0, -100)    # starting from 1, instead of 0

    def size(self):
        return len(self.my_list)

    def insert(self, data):
        curr_size = self.size()
        idx = curr_size

        self.my_list.append(data)
        # for node: i, the parent node is i //2
        while idx // 2 >= 1 and self.my_list[idx] > self.my_list[idx//2]:
            self.swap(idx, idx // 2)
            idx = idx // 2

    def remove_max(self):       # it means to remove the top node
        if self.size() == 1:
            return -1

        # step1 pop the root node
        max_node = self.my_list.pop(1)  # return the root node

        # step 2: heapify the remaining nodes
        cur_tail = self.my_list.pop(-1)
        self.my_list.insert(1, cur_tail)
        self.heapify(self.size()-1, i=1)

    def build_heap(self):
        # from the last non-leaf point
        # since the last point index is self.size() or len (self.list), its parent (//2) is the last non-leaf point
        last_non_leaf_idx = self.size() // 2
        for i in range(last_non_leaf_idx, 0, -1):
            self.heapify(self.size()-1, i)

    def heap_sort(self):
        self.build_heap()
        k = self.size() - 1
        while k > 1:
            self.swap(1, k)
            k -= 1
            self.heapify(k, 1)

    # n is the length of the list to heap
    def heapify(self, n, i):
        # from the i-th node to do heapify
        while True:
            max_pos = i
            if 2 * i <= n and self.my_list[i] < self.my_list[2 * i]:
                max_pos = 2 * i
            if 2 * i + 1 <= n and self.my_list[max_pos] < self.my_list[2 * i + 1]:
                max_pos = 2 * i + 1

            if max_pos == i:
                break
            else:
                self.swap(i, max_pos)
                i = max_pos

    def swap(self, i, j):
        my_list = self.my_list
        tmp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = tmp

        return

# ini_list = [33, 27, 21, 16, 13, 15, 9, 5,6,7,8,1,2]
# heap = my_heap(ini_list)
# heap.insert(22)
# print(heap.my_list)
# heap.remove_max()
# print(heap.my_list)

# Test building heap
ini_list = [7, 5, 19, 8, 4, 1, 20, 13, 16]
# ini_list = [5, 4, 1]
heap = my_heap(ini_list)
# heap.build_heap()
# print(heap.my_list)
heap.heap_sort()
print(heap.my_list)

