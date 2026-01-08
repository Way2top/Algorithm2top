import bisect
from collections import defaultdict
class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.position = defaultdict(list)
        for i, x in enumerate(arr):
            self.position[x].append(i) # position[x] 表示 x 在 arr 中出现的位置的下标（一个列表）  另外，position[x] 一定是升序的

    def query(self, left: int, right: int, value: int) -> int:
        a = self.position[value]
        return bisect.bisect_right(a, right) - bisect.bisect_left(a, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)