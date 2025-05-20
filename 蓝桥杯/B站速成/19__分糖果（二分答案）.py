# 力扣：2226. 每个小孩最多能分到多少糖果
from typing import List


def maximumCandies(candies: List[int], k: int) -> int:
    n = len(candies)
    lo = 0
    hi = max(candies)

    def check(res):
        return sum(x // res for x in candies) < k

    while lo < hi:
        mid = (lo + hi) // 2
        # 如果check(mid)为True，那么说明sum(x // res for x in candies) < k成立，也就是说每一堆糖果太多了，堆数少了不够分，所以要减小每一堆的糖果数量
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo - 1


ans = maximumCandies([5, 8, 6], 3)
print(ans)
