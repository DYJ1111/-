class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 新建链表
        if not l1:
            return l2
        if not l2:
            return l1
        # dummy = ListNode(0)
        # cur = dummy
        # p1 = l1
        # p2 = l2
        #
        # while p1 and p2:
        #     if p1.val < p2.val:
        #         cur.next = p1
        #         p1 = p1.next
        #     else:
        #         cur.next = p2
        #         p2 = p2.next
        #     cur = cur.next
        #
        # cur.next = p1 if p1 else p2
        #
        # return dummy.next
        dummy = ListNode(0)
        cur = dummy
        cur.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next