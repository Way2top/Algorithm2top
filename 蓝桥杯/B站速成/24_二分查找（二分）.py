# 力扣：704. 二分查找
from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1


print(search([-1, 0, 3, 5, 9, 12], 2))
