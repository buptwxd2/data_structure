class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


def pre_order(root_node):
    if not root_node:
        return

    print (root_node.value)
    pre_order(root_node.left)
    pre_order(root_node.right)


def in_order(root_node):
    if not root_node:
        return

    in_order(root_node.left)
    print(root_node.value)
    in_order(root_node.right)


def post_order(root_node):
    if not root_node:
        return

    post_order(root_node.left)
    post_order(root_node.right)
    print(root_node.value)


a_node = TreeNode('A')
b_node = TreeNode('B')
c_node = TreeNode('C')
d_node = TreeNode('D')
e_node = TreeNode('E')
f_node = TreeNode('F')
g_node = TreeNode('G')


a_node.set_left(b_node)
a_node.set_right(c_node)

b_node.set_left(d_node)
b_node.set_right(e_node)

c_node.set_left(f_node)
c_node.set_right(g_node)

print (pre_order(a_node))

print(in_order(a_node))

print(post_order(a_node))
