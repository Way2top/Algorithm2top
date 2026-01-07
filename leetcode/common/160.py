from structure import ListNode
from typing import Optional

# 当我在我的路上走过一遍依然没有遇见你时，那么我会接着来到你走过的路走一遍，如果我们心有灵犀，那么我们终将相遇
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 如果任一链表为空，则直接返回None
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        # 两个指针同步走，当他们相等时即为焦点
        while pA is not pB:
            # A走完B就从头开始走，B走完A就从头开始走
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA # 或 pB 都一样