# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# if I wanna definition for double-Linked list.
#      def __init__(self,val=0, next=None, prev=None):
#          self.val = val
#          self.next = next
#          self.prev = prev

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

# edge case: only list1 == None, only list2 == None, both list1 and list2 == None



        
            

        