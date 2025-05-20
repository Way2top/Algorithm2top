# 力扣：1

def twoSum(self, nums: list[int], target: int) -> list[int]:
    n = len(nums)

    # Version 1：纯粹的暴力
    # for i in range(n):
    #     for j in range(n):
    #         if i == j:
    #             continue
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # Version 2：带点脑子的暴力
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # Version 3：哈希，牛逼
    # 创建一个字典，key存nums的值，value存下标
    dic = {}
    for i, n in enumerate(nums):
        if target - n in dic:
            return [i, dic[target - n]]
        dic[n] = i

