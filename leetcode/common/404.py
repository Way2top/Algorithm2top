from structure import TreeNode
from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        if root.left and root.left.left is None and root.left.right is None:
            res += root.left.val
        return res