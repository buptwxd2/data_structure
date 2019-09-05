class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

# assume this binary search tree has been built already
class binary_search_tree:
    def __init__(self, root_node):
        self.root_node = root_node

    def find(self, data):
        node = self.root_node
        while node:
            if node.value == data:
                return node
            elif node.value < data:
                node = node.right
            elif node.value > data:
                node = node.left

        return None

    # here just consider the situation where inserted_data does not yet exist
    def insert(self, data):
        new_node = Node(data)

        if not self.root_node:
            self.root_node = new_node
            return

        node = self.root_node
        while node:
            if node.value < data:
                if not node.right:
                    node.right = new_node
                    return
                else:
                    node = node.right

            else:
                if not node.left:
                    node.left = new_node
                    return
                else:
                    node = node.left

    def delete(self, data):
        node = self.root_node
        parent_node = None  # parent_node is the parent of target node

        # First find the node whose value equals data
        while node and node.value != data:
            parent_node = node
            if node.value > data:
                node = node.left
            else:
                node = node.right

        if not node:
            return -1  # didn't find the target node

        if node.left and node.right:
            min_node = node.right
            parent_min_node = node
            while min_node.left:
                parent_min_node = min_node
                min_node = min_node.left

            # substitute the node using min node
            node.value = min_node.value
            node = min_node
            parent_node = parent_min_node

        # found the target node
        if not node.left:
            child = node.right
        elif not node.right:
            child = node.left

        if not parent_node: # target node is root node
            self.root_node = child
        elif parent_node.left == node:
            parent_node.left = child
        else:
            parent_node.right = child


def in_order(root_node):
    if not root_node:
        return

    in_order(root_node.left)
    print(root_node.value)
    in_order(root_node.right)


def search_node(root_node, data):
    if not root_node:
        return None

    if root_node.value == data:
        return root_node
    elif root_node.value < data:
        return search_node(root_node.right, data)
    elif root_node.value > data:
        return search_node(root_node.left, data)

# build this binary search tree
a_node = Node(33)
b_node = Node(17)
c_node = Node(50)
d_node = Node(13)
e_node = Node(18)
f_node = Node(34)
g_node = Node(58)
h_node = Node(16)
i_node = Node(25)
j_node = Node(51)
k_node = Node(66)
l_node = Node(19)
m_node = Node(27)

a_node.set_left(b_node)
a_node.set_right(c_node)

b_node.set_left(d_node)
b_node.set_right(e_node)

c_node.set_left(f_node)
c_node.set_right(g_node)

d_node.set_right(h_node)

e_node.set_right(i_node)

g_node.set_left(j_node)
g_node.set_right(k_node)

i_node.set_left(l_node)
i_node.set_right(m_node)


bs_tree = binary_search_tree(a_node)
in_order(a_node)
# print(search_node(a_node, 67).value)
print(bs_tree.find(27).value)

# bs_tree.insert(55)
# in_order(a_node)
# print(bs_tree.find(55).value)


print("Testing Delete")
bs_tree.delete(50)
in_order(a_node)

# empty_tree = binary_search_tree(None)
# empty_tree.insert(3)
# empty_tree.insert(1)
# empty_tree.insert(5)
# empty_tree.insert(0)
# empty_tree.insert(2)
# empty_tree.insert(4)
# empty_tree.insert(6)
# root_node = empty_tree.root_node
# in_order(root_node)
