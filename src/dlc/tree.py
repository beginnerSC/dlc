from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """226. Invert Binary Tree"""
    if not root:
        return root
    else:
        return TreeNode(root.val, invertTree(root.right), invertTree(root.left))
