from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """102. Binary Tree Level Order Traversal"""
    if not root: 
        return []

    q = deque([root])

    res = []
    while q:
        n = len(q)
        level = []
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level)
    
    return res


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """226. Invert Binary Tree"""
    if not root:
        return root
    else:
        return TreeNode(root.val, invertTree(root.right), invertTree(root.left))
