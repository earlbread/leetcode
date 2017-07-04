/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        if head == nil {
            return nil
        }

        var prev: ListNode? = nil

        var curr = head
        var next = curr?.next

        while next != nil {
            curr?.next = prev
            prev = curr
            curr = next
            next = curr?.next
        }

        curr?.next = prev

        return curr
    }

    func isPalindrome(_ head: ListNode?) -> Bool {
        if head == nil || head?.next == nil {
            return true
        }

        var slow = head
        var fast = head

        while fast != nil && fast?.next != nil {
            fast = fast?.next?.next
            slow = slow?.next
        }

        if fast != nil {
            slow = slow?.next
        }

        var back = reverseList(slow)
        var front = head

        while front != nil && back != nil {
            if front?.val != back?.val {
                return false
            }
            front = front?.next
            back = back?.next
        }
        return true
    }
}
