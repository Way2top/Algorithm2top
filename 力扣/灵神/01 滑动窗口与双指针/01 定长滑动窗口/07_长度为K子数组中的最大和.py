# Leetcode：2461
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0
        total = 0
        dic = {}

        # 初始化第一个窗口
        for i in range(k):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            total += nums[i]
        if len(dic) == k:
            res = total

        # 往后滑动
        for i in range(1, n-k+1):
            # 处理丢弃元素
            total -= nums[i-1]
            dic[nums[i-1]] -= 1
            if dic[nums[i-1]] == 0:
                del dic[nums[i-1]]

            # 处理新增元素
            total += nums[i-1+k]
            dic[nums[i-1+k]] = dic.get(nums[i-1+k], 0) + 1

            # 判断是否满足元素各不相同
            if len(dic) == k:
                res = max(res, total)
        return res
