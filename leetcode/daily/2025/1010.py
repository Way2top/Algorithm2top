# leetcode:3147
import math
class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        for i in range(n - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)