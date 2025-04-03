class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class palindromeLinklist:
    def isPalindrome(self, head: ListNode) ->bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse second half

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        #check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

