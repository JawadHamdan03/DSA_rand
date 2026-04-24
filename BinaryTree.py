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

root= Node(5)
a= Node(6)
b= Node(3)
c= Node(4)
d= Node(8)

add_node_BST(root,a)
add_node_BST(root,b)
add_node_BST(root,c)
add_node_BST(root,d)
inorder_tree_traversal(root)




