from bisect import bisect_left, bisect_right

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # 也就是说对于 arr1[i]，任意 arr2[j] 与其差值都需要大于 d，那么 arr1[i] 就算一个距离
        arr2.sort()
        ans = 0
        n = len(arr2)
        for x in arr1:
            t1 = abs(x - d) 
            t2 = x + d
            n1 = bisect_left(arr2, t1) - 1
            n2 = n - bisect_right(arr2, t2)
            if n1 + n2 == n:
               ans += 1
        return ans 

            