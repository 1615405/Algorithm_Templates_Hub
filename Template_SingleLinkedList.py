# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    合并两个已排序的链表，并返回一个新的排序链表。新链表是通过将两个链表的节点依次连接而成的。
    
    参数：
        list1 (Optional[ListNode]): 第一个排序链表。
        list2 (Optional[ListNode]): 第二个排序链表。
    
    返回：
        Optional[ListNode]: 合并后的排序链表的头节点。
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

    参数：
        head (Optional[ListNode]): 排序链表的头节点。
    
    返回：
        Optional[ListNode]: 删除重复元素后的链表的头节点。
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

    参数：
        head (Optional[ListNode]): 链表的头节点。
    
    返回：
        bool: 如果链表中有环，则返回True；否则返回False。
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
    
    参数：
        headA (ListNode): 第一个链表的头节点。
        headB (ListNode): 第二个链表的头节点。
    
    返回：
        Optional[ListNode]: 两个链表相交的节点，如果不相交，则返回 None。
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

    参数：
        head (Optional[ListNode]): 链表的头节点。
        val (int): 需要删除的节点值。
    
    返回：
        Optional[ListNode]: 删除指定值节点后的链表头节点。
    """
    dummy = cur = ListNode(next=head)
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
