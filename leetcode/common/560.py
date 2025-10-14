from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 求出前缀和数组J
        prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        # 按题目要求，就是要找出所有的 i, j(i < j),满足 prefix[j] - prefix[i] = k
        # 那么我们可以知道 prefix[i] = prefix[j] - k
        # 对于暴力算法，我们外层循环遍历 j，然后 内层循环 i 在 j 的前面去找出来所有的 i
        # 对于优化的办法，我们把内层循环使用哈希表优化到 O(1)
        # 既然暴力这样做不会漏，那么优化方法也不会漏
        
        # dic[x] 的含义是 x 的个数
        dic = defaultdict(int) # 这里使用 defaultdict 是为了防止取到不存在的数字报错
        res = 0
        # 这里的 p 是上面讲到的 prefix[j]
        for p in prefix: # 外层循环
            res += dic[p - k] # 内层循环用哈希表优化
            dic[p] += 1
        return res
