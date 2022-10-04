# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        tail = res
        c = 0
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            addition = v1 + v2 + c
            c = 0
            if addition > 9:
                c = 1
                addition -= 10
            tail.next = ListNode(addition)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            tail = tail.next
        return res.next
