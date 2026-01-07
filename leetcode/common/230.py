from structure import TreeNode
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 给的是二叉搜索树，中序遍历是有序的（从小到大）
        # 现在求第 k 小的元素，实际上就是中序遍历的结果的第 k 个元素
        ans = 0

        def dfs(node: TreeNode):
            nonlocal k, ans
            if node is None or k == 0:
                return
            dfs(node.left)
            k -= 1
            if k == 0:
                ans = node.val
            dfs(node.right)

        dfs(root)
        return ans
