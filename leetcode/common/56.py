# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         intervals.sort(key=lambda x: x[0])
#         res = []

#         for interval in intervals:
#             if res and res[-1][1] >= interval[0]:
#                 res[-1][1] = max(res[-1][1], interval[1])
#             else:
#                 res.append(interval)
#         return res


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # 先把所有区间都记录下来
        points = []
        for start, end in intervals:
            points.append((start, 'l'))
            points.append((end, 'r'))
        
        points.sort()
        
        stack = []
        res = []
        start_of_merge = 0

        for point, direction in points:
            if not stack:
                start_of_merge = point
            if direction == 'l':
                stack.append('l') 
            else:
                stack.pop()
            
            if not stack:
                res.append([start_of_merge, point])
        return res

s = Solution()
ans = s.merge([[1,3],[2,6],[8,10],[15,18]])
print(ans)
        