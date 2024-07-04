# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode()
    carry = 0
    while carry or l1 or l2:
        carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next



def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if list1 else list2

        return dummy.next



def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    pre, cur = None, head
    while cur:
        cur_next = cur.next
        cur.next = pre
        pre = cur
        cur = cur_next
    return pre