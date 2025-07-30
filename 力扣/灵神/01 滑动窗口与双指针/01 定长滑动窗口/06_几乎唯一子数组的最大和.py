# Leetcode：2841
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        n = len(nums)
        dic = {}
        res = 0
        total = 0

        # 初始化第一个滑动窗口
        for i in range(k):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            total += nums[i]
        if len(dic) >= m:
            res = total

        # 往后滑动
        for i in range(1, n - k + 1):
            # 丢弃元素处理
            dic[nums[i - 1]] -= 1
            total -= nums[i-1]
            if dic[nums[i - 1]] == 0:
                del dic[nums[i-1]]

            # 新增元素处理
            dic[nums[i - 1 + k]] = dic.get(nums[i - 1 + k], 0) + 1
            total += nums[i - 1 + k]
            if len(dic) >= m:
                res = max(res, total)
        return res
