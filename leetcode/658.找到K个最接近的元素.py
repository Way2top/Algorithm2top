class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # 1, 2, 3, 4, 5
        # x = 3, target = 4
        left = 0
        right = len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : right + k]
