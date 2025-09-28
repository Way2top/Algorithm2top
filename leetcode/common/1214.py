from structure import TreeNode
from typing import Optional

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        res = False
        def traversal(node: TreeNode) -> list[int]:
            if node is None:
                return []
            arr = []
            arr.extend(traversal(node.left))
            arr.extend(traversal(node.right))
            arr.append(node.val)
            return arr
        r1 = traversal(root1)
        r2 = traversal(root2)
        for v in r1:
            if target - v in r2:
                return True
        return False