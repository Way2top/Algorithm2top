class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        total = 0
        res = 0
        n = len(customers)
        # initialize total's val
        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i]
        # initialize the first window
        for i in range(minutes):
            if grumpy[i] == 1:
                total += customers[i]
        res = total
        # keep moving
        for i in range(1, n - minutes + 1):
            # handing the discarded elements
            if grumpy[i - 1] == 1:
                total -= customers[i - 1]
            # handing the new elements
            if grumpy[i - 1 + minutes] == 1:
                total += customers[i - 1 + minutes]
            res = max(total, res)
        return res
