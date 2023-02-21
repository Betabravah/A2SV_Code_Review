# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       
        dummy = ListNode(0, slow)
        ptr = dummy.next
        cur = ptr.next
        while cur:
            nextNode = cur.next
            cur.next = ptr
            ptr, cur = cur, nextNode
        slow.next = None

        maxSum = 0
        list1, list2 = head, ptr
        print(dummy.next)
        while list1 and list2:
            sum = list1.val + list2.val
            maxSum = max(maxSum, sum)
            list1 = list1.next
            list2 = list2.next
        
        return maxSum
