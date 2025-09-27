from structure import TreeNode
from typing import Optional

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # 根据题意，root 不会为空
        minVal = root.val
        res = 0
