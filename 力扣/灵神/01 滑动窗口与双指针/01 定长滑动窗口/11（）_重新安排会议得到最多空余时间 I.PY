class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        meeting = 0
        n = len(startTime)
        for i in range(n):
            meeting += endTime[i] - startTime[i]
        res = eventTime - meeting
        return res