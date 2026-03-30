# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Step 1: slow = fast = 3 
# Step 2: slow = 2 and fast = 0
# Step 3: slow = 0 and fast = 2
# Step 4: slow = -4 and fast = -4
# slow = 3 and fast = -4
# slow = 2 and fast 2 

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head 
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
            

       
            



