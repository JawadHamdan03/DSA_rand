from typing import List
from collections import deque
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

def BFS_iterative(root):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        length = len(queue)
        for i in range(length):
            curr=queue.popleft()
            print(curr.val)
            if curr.left :
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


#------------------------------- Sum all nodes in Tree --------------------
def sum_tree_DFS(root:Node, sum=0):
    if not root :
        return sum

    sum+=root.val
    return sum_tree_DFS(root.left,sum)+sum_tree_DFS(root.right)


def sum_tree_BFS(root:Node):
    if not root:
        return
    sum=0
    queue = deque()
    queue.append(root)

    while queue:
        length = len(queue)
        curr= queue.popleft()
        sum+=curr.val
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return sum


# ----------------------------- find target in a tree --------
##DFS
def find_target_recursive(root:Node,target:int):
    if not root :
        return False
    if root.val==target:
        return True
    return find_target_recursive(root.left,target) or find_target_recursive(root.right,target)

##BFS
def find_target_iterative(root:Node,target:int):
    if not root :
        return False
    queue= deque([root])

    while queue:
        length = len(queue)
        curr = queue.popleft()
        if curr.val==target :
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return False

##----------------------------- tree min value -------------------
## DFS
min_value =1000000000000
def tree_min_recursive(root : Node):
    if not root :
        return
    global min_value
    min_value=min(root.val,min_value)
    tree_min_recursive(root.left)
    tree_min_recursive(root.right)
    return min_value


#BFS
def tree_min_iterative(root:Node):
    min_value=1000000000000
    if not root :
        return
    queue= deque([root])

    while queue:
        length= len(queue)
        curr = queue.popleft()
        min_value=min(min_value,curr.val)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return min_value


## ---------------------max Root to leaf ---------------
def max_root_leaf(root:Node,counter=1):
    if not root:
        return counter-1
    return max(max_root_leaf(root.left,counter+1),max_root_leaf(root.right,counter+1))


## --------------- max Sum from root to leaf-------

def max_sum_root_leaf(root:Node,sum=0):
    if not root :
        return sum
    return max(max_sum_root_leaf(root.right,sum+root.val),max_sum_root_leaf(root.left,sum+root.val))


#------------------------------ Run Tests----------------

# Construct Tree
tree= Node(5)
my_nodes=[Node(6),Node(3),Node(4),Node(8),Node(2),Node(9),Node(10)]
create_BST(tree,my_nodes)

# Traversing DFS and BFS
##DFS_recursive(tree)
##DFS_iterative(tree)
#BFS_iterative(tree)

# Sum of tree
#res1=sum_tree_DFS(tree)
#res2=sum_tree_BFS(tree)
#print(res1)
#print(res2)

# Find Target
#res=find_target_recursive(tree,9)
#res2=find_target_iterative(tree,9)
#print(res)
#print(res2)

# Tree min
#res=tree_min_recursive(tree)
#res2=tree_min_iterative(tree)
#print(res)
#print(res2)

# max count root to leaf
res=max_root_leaf(tree)
print(res)


# max sum from root to leaf
res2= max_sum_root_leaf(tree)
print(res2)