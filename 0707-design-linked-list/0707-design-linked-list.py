class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        curr = self.head

        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next

        return curr.val if curr else -1

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head

        for _ in range(index - 1):
            if not curr:
                return
            curr = curr.next

        if not curr:
            return

        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node

    def deleteAtIndex(self, index):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head

        for _ in range(index - 1):
            if not curr.next:
                return
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next