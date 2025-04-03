from typing import Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class twoSumBSTs:

    def storeTreeValues(self, root: Optional[TreeNode], values: Set[int]) ->None:
        if root:
            values.add(root.val)
            self.storeTreeValues(root.left, values)
            self.storeTreeValues(root.right, values)

    def searchComplement(self, root: Optional[TreeNode], values: Set[int], target: int) -> bool:
        if root is None:
            return False
        complement = target - root.val
        if complement in values:
            return True
        # Recursively check left and right subtrees
        return self.searchComplement(root.left, values, target) or \
            self.searchComplement(root.right, values, target)


    def twoSumBSTs(self, root1, root2, target) -> bool:
        values = set()
        self.storeTreeValues(root1, values)
        return self.searchComplement(root2, values, target)