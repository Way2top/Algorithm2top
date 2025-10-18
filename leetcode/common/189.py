class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = nums * 2
        res = arr[n - k%n : 2 * n - k%n]
        for i in range(n):
            nums[i] = res[i]