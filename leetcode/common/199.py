from structure import TreeNode
from collections import deque
from typing import Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while len(q) > 0:
            levelSize = len(q)
            for i in range(levelSize):
                cur = q.popleft()
                if i == levelSize - 1:
                    ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return ans

