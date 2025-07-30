# Leetcode:2105
class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        left = 0
        right = n - 1
        full_A = capacityA
        full_B = capacityB
        count = 0
        while left <= right:
            if left == right:
                choose = max(capacityA, capacityB)
                if choose < plants[left]:
                    count += 1
                    break
                break
            
            if capacityA >= plants[left]:
                capacityA -= plants[left]
                left += 1
            else:
                count += 1
                capacityA = full_A - plants[left]
                left += 1

            if capacityB >= plants[right]:
                capacityB -= plants[right]
                right -= 1
            else:
                count += 1
                capacityB = full_B - plants[right]
                right -= 1
        return count
            
s = Solution()
ans = s.minimumRefill([2,1,1], 2, 2)
print(ans)