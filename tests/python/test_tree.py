"""Unit tests for tree functions."""
from dlc.tree import TreeNode, invertTree


def tree_to_array(root, level_order=True):
    """Helper: Convert tree to array representation."""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def array_to_tree(arr):
    """Helper: Convert array to tree."""
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root


class TestInvertTree:
    def test_basic_inversion(self):
        """Test inverting a basic tree."""
        root = array_to_tree([4, 2, 7, 1, 3, 6, 9])
        result = invertTree(root)
        assert tree_to_array(result) == [4, 7, 2, 9, 6, 3, 1]
    
    def test_empty_tree(self):
        """Test inverting an empty tree."""
        assert invertTree(None) is None
    
    def test_single_node(self):
        """Test inverting a single node tree."""
        root = array_to_tree([1])
        result = invertTree(root)
        assert tree_to_array(result) == [1]
