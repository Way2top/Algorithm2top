class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic.keys():
                return [i, dic[target - nums[i]]]
            dic[nums[i]] = i
        return [0, 0]
