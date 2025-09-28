class Solution:
    def isPreorder(self, nodes: list[list[int]]) -> bool:
        stack = [-1]
        for node, parent in nodes:
            while stack and stack[-1] != parent:
                stack.pop()
            if stack is None:
                return False
            stack.append(node)
        return True

s = Solution()
res = s.isPreorder([[0,-1],[1,0],[2,0],[3,2],[4,2]])