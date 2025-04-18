class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class hasCycle:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False