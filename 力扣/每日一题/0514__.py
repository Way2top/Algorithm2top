class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        dp = [1] * 26
        stored_dp = []

        for _ in range(26):
            new_dp = [0] * 26
            