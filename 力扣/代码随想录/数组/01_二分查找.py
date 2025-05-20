# Leetcode:704
# class Solution:
#     def search(self, num:list[int], target:int) -> int:
#         n = len(num)
#         lo = 0
#         hi = n
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if target > num[mid]:
#                 lo = mid + 1
#             elif target < num[mid]:
#                 hi = mid
#             else:
#                 return mid 
#         return -1
class Solution:
    def search(self, num:list[int], target:int) -> int:
        n = len(num)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target > num[mid]:
                lo = mid + 1
            elif target < num[mid]:
                hi = mid - 1
            else:
                return mid
        return -1
