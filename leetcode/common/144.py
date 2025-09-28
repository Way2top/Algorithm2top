from typing import Optional

from structure import TreeNode

# 方法1：递归
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
#         if root is None:
#             return []
#         res = []
#         def recursionOrder(node: Optional[TreeNode]):
#             if node is None:
#                 return
#             res.append(node.val)
#             recursionOrder(node.left)
#             recursionOrder(node.right)
#         recursionOrder(root)
#         return res

# 方法2：模拟
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        # 入栈顺序：右左中
        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack[-1]
            stack = stack[:-1]
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res