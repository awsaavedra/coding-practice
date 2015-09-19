/*
Alexander Saavedra
LeetCode Problem: MergeTwoSortedLists
"Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first 
two lists."
Notes:

This is a very standard solution, I will come back to this
with a more novel one if I have time
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode tmp = new ListNode(0);
        ListNode prev = tmp;
        while( l2 != null && l1 != null){
            if(l1.val>l2.val){
                prev.next = l2;
                l2 = l2.next;
            }else{
                prev.next = l1;
                l1 = l1.next;
            }
            prev = prev.next;
        }
        if( l1 != null)
            prev.next = l1;
        else if( l2 != null)
            prev.next = l2;
        return tmp.next;
    }
}
