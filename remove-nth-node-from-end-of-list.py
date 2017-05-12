# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head

        for i in range(n):
            curr = curr.next

        if curr == None:
            head = head.next
            return head

        prev = head

        while curr.next != None:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next

        return head

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    head = s.removeNthFromEnd(head, 2)

    curr = head

    while curr != None:
        print(curr.val)
        curr = curr.next
