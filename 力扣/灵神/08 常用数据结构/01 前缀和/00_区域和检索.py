# Leetcode:303
class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

numarray = NumArray([-2, 0, 3, -5, 2, -1])
res = numarray.sumRange(2, 5)
print(res)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)