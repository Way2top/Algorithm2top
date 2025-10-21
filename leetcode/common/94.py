from structure import TreeNode
from typing import Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        
        stack = []
        res = []
        while len(stack) > 0 or root is not None:
            # 让当前指针一直走到树的最左子节点
            while root:
                stack.append(root)
                root = root.left
            
            top = stack.pop()
            res.append(top.val)
            root = top.right
        return res