from structure import TreeNode
from typing import Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        # 中序遍历：左中右
        stack = []
        res = []
        # Step1：走到整棵树最左节点
        curr = root
        while len(stack) > 0 or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            node = stack[-1]
            stack = stack[:-1]
            res.append(node.val)
            curr = node.right
        return res