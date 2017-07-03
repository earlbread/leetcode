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

        var curr = head
        var prev: ListNode? = nil
        var next = curr!.next

        while (next != nil) {
            curr!.next = prev
            prev = curr
            curr = next
            next = next!.next
        }
        curr!.next = prev

        return curr
    }
}
