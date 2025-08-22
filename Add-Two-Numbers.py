# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        l2_str = ""

        #l1
        while l1.next is not None:
            l1_str += str(l1.val)
            l1 = l1.next
        l1_str += str(l1.val)
        l1_str = l1_str[::-1]

        #l2
        while l2.next is not None:
            l2_str += str(l2.val)
            l2 = l2.next
        l2_str += str(l2.val)
        l2_str = l2_str[::-1]

        print(l1_str)
        print(l2_str)

        summed = int(l1_str) + int(l2_str)

        print(summed)

        retList = ListNode()
        current = retList
        for d in str(summed)[::-1]:
            current.next = ListNode(int(d))
            current = current.next
        return retList.next