from structure import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode|None:
        if not nums:
            return None
        m = len(nums) // 2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m+1:])
        return TreeNode(nums[m], left, right)
        