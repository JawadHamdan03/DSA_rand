class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 226. Invert Binary Tree

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    temp = root.left
    root.left=root.right
    root.right=temp

    invertTree(root.left)
    invertTree(root.right)



## 104. Maximum Depth of Binary Tree
count=0
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root :
        return 0
        
    return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
        


## 100. Same Tree
def isSameTree(p:TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if (not p and  q )or(p and not q) :
        return False
    if p.val != q.val:
        return False
        
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
