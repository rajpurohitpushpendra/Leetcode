class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        right = ListNode(0)
        l, r = left, right

        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next

        r.next = None
        l.next = right.next

        return left.next