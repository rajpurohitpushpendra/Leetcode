class Solution:
    def splitListToParts(self, head, k):
        # Count nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        size = n // k
        extra = n % k

        result = []

        for i in range(k):
            part_size = size + (1 if i < extra else 0)
            part_head = head

            # Move to the end of this part
            for j in range(part_size - 1):
                head = head.next

            if head:
                next_part = head.next
                head.next = None
                head = next_part

            result.append(part_head)

        return result