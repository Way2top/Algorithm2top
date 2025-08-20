#
# @lc app=leetcode.cn id=2080 lang=python3
#
# [2080] 区间内查询数字的频率
#
from collections import defaultdict
from bisect import bisect_left, bisect_right
# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos
    def query(self, left: int, right: int, value: int) -> int:
        x = self.pos[value] # x 为下表列表
        return bisect_right(x, right) - bisect_left(x, left)
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

