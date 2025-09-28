from structure import TreeNode
from typing import Optional

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack[-1]
            stack = stack[:-1]
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res.reverse()
        return res