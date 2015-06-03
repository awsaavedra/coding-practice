/*
Alexander Saavedra
github: awsaavedra
Problem:
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        if(head == null)
            return null;
        ListNode a = head; //cycle pointer 1
        ListNode b = head; //cycle pointer 2
        ListNode c = head; //previous value pointer, for a
        while( a != null && b != null){
            a = a.next;
            if( b.next == null)
                return null;
            else
                b = b.next.next;
            if( a == b){ 
                while( c != a){
                    a = a.next;
                    if( a == b){
                        c = c.next;
                    }
                }
                return c;
            }
        }
        return null;
    }
}
