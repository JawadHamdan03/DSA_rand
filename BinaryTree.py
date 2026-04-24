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

def inorder_tree_traversal(root):
    if not root:
        return
    inorder_tree_traversal(root.left)
    print(root.val)
    inorder_tree_traversal(root.right)

def create_BST(root:Node , nodes:List):
    for node in nodes:
        add_node_BST(root,node)




root= Node(5)
nodes=[Node(6),Node(3),Node(4),Node(8)]
create_BST(root,nodes)
inorder_tree_traversal(root)




