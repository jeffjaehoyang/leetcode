# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Trick is to create a list node to start with.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        result = head
        a, b = list1, list2
        while a and b:
            target = a if a.val <= b.val else b
            if target is a:
                a = a.next
            else:
                b = b.next
            head.next = target
            head = head.next

        while a:
            head.next = a
            head = head.next
            a = a.next

        while b:
            head.next = b
            head = head.next
            b = b.next

        return result.next
