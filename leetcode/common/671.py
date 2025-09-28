import math

from structure import TreeNode
from typing import Optional

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # 根据题意，root 不会为空
        minVal = root.val
        res = math.inf
        def postOrder(node: TreeNode):
            if node is None:
                return
            if node.val > minVal:
                nonlocal res
                res = min(res, node.val)
            postOrder(node.left)
            postOrder(node.right)
        postOrder(root)
        if res == math.inf:
            return -1
        else:
            return res

