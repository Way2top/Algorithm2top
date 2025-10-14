import math
from collections import deque

# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         res = []
#         window = {}
#         maxVal = -math.inf

#         # 初始化第一个窗口
#         for i in range(k):
#             window[nums[i]] = window.get(nums[i], 0) + 1
#             maxVal = max(maxVal, nums[i])
#         res.append(maxVal)

#         # 往后走
#         left = 0
#         for right in range(k, len(nums)):
#             leftVal = nums[left]
#             window[leftVal] -= 1
#             if window[leftVal] == 0:
#                 del window[leftVal]

#             rightVal = nums[right]
#             window[rightVal] = window.get(rightVal, 0) + 1

#             # 如果左端点删去的元素是最大值，那么最大值没了，需要再删除后的元素中找最大值
#             if maxVal == leftVal:
#                 maxVal = max(window.keys()) # 性能瓶颈导致超时
#             left += 1


#             maxVal = max(maxVal, rightVal)

#             res.append(maxVal)
#         return res

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        对于本题来说，希望能有一个结构能够记录遍历到当前窗口为止最大的元素
        滑动窗口需要考虑三件事情，右端进入窗口，左端滑出窗口，记录答案
        我们需要一个额外的数据结构来记录答案，上面的暴力做法我们已经知道了瓶颈所在
        瓶颈在于：当左端出窗口的时候，如果出的元素是最大值，那么我们需要在剩余的窗口中使用 O(N) 的 max 方法找到最大值，这导致时间复杂度变成了 N 的平方
        因此我们希望有一个数据结构能够很方便地用常数级的时间找到最大值，另外，我们还频繁涉及两端的增删操作
        两端增删可以马上联想到队列，但是，队列似乎不能常数级找到最大值吧
        但是如果，我们维持队列的单调性，让这个队列始终保持递减，那么我们就可以直接取出队列的第一个元素作为最大值添加到答案中
        至此，我们已经可以基本确定，本题这个额外记录答案的数据结构就应该是一个单调队列
        那为什么不是普通的队列而是双端队列呢？因为我们窗口在滑动的过程中，两端都涉及增删
        接下来就可以按照这个思路开始写代码了
        
        """
        q = deque() # 其中记录的都是下标
        res = [0] * (len(nums) - k + 1)
        # 从前往后遍历 nums，在便利的过程中维护 deque
        for i, x in enumerate(nums):
            # 1. 怎么入窗口
            # 如果 deque 没元素，直接加；如果有元素，那么新的元素和 q[-1] 比较，如果大于 q[-1]，那么 q[-1] 没有任何机会成为窗口中的最大元素了（因为我们一直往前走，然后遇到了一个比刚刚走过去的元素还要大的元素），此时我们弹出 q[-1] 然后加入这个比原来 q[-1] 大的元素
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i) 

            # 2. 怎么出窗口
            # 我们需要确保窗口长度为 k
            left = i - k + 1 # 窗口左端点
            if q[0] < left: # i 就是右边界，q[0] 就是左边界
                q.popleft()
            
            # 3. 何时记录答案
            if left >= 0: # 窗口左端点处记录答案
                res[left] = nums[q[0]]
            
        return res
        