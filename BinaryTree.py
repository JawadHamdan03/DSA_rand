from typing import List

class Node :
    def __init__(self,val: int, right:Node=None, left:Node = None):
        self.val= val
        self.right=right
        self.left=left

def add_node_BST(root, node):
    if not root:
        return

    if node.val<root.val:
        if root.left is None:
            root.left=node
        else :
            add_node_BST(root.left,node)

    elif node.val>root.val:
        if root.right is None:
            root.right=node
        else :
            add_node_BST(root.right,node)

def create_BST(root, nodes):
    for node in nodes:
        add_node_BST(root,node)

def DFS_recursive(root):
    if not root:
        return
    DFS_recursive(root.left)
    print(root.val)
    DFS_recursive(root.right)

def DFS_iterative(root):
    if not root:
        return
    stack =[root]
    values:List =[]
    while stack:
        curr = stack.pop()
        values.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    print(*values)


tree= Node(5)
my_nodes=[Node(6),Node(3),Node(4),Node(8),Node(2)]
create_BST(tree,my_nodes)
DFS_recursive(tree)
DFS_iterative(tree)

