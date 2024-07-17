# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    合并两个已排序的链表，并返回一个新的排序链表。新链表是通过将两个链表的节点依次连接而成的。
    """
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


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    删除排序链表中的所有重复元素，使每个元素只出现一次，并返回修改后的链表的头节点。
    """
    if not head:
        return None
    cur = head
    while cur.next:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def hasCycle(head: Optional[ListNode]) -> bool:
    """
    判断链表中是否有环。使用快慢指针方法，快指针每次移动两步，慢指针每次移动一步，如果链表有环，则快慢指针最终会相遇。
    """
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True
    return False


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    寻找两个单链表相交的起始节点。如果两个链表没有交点，返回 None。
    使用两个指针分别遍历两个链表，当达到链表末尾时，转向另一个链表的头部继续遍历，直到两个指针相遇。
    """
    A, B = headA, headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA
    return A


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    从链表中删除所有值等于指定值 val 的节点。
    使用虚拟头节点简化边界条件处理，确保即使头节点需要被删除时也能正确处理。
    """
    dummy = cur = ListNode(next=head)
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


def isPalindrome(head: Optional[ListNode]) -> bool:
    """
    判断给定的链表是否为回文链表。使用快慢指针找到链表中点，然后翻转后半部分，之后比较前半部分和翻转后的后半部分是否相同。
    """
    def middleList(head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            cur_next = current.next
            current.next = previous
            previous = current
            current = cur_next
        return previous
        
    first = head
    second = reverseList(middleList(head))
    while second:
        if second.val != first.val:
            return False
        second = second.next
        first = first.next
    return True


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    对两个表示非负整数的单链表进行求和。链表的每个节点包含一个数字，数字以逆序方式存储，每个节点只能存储一位数字。
    例如，(2 -> 4 -> 3) + (5 -> 6 -> 4) 应该返回 (7 -> 0 -> 8)，因为 342 + 465 = 807。
    """
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
