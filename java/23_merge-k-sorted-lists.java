/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // edgecases
        if(lists.length == 0){
            return null;
        }else{
            return mergeK(Arrays.asList(lists)).get(0);
        }
    }

    public List<ListNode> mergeK(List<ListNode> lists){
        if(lists.size() <= 1){
            return lists;
        }else{
            List<ListNode> subLists = new ArrayList<ListNode>();
            for(int i = 0; i < lists.size(); i++) {
                if(i+1 < lists.size()){
                    subLists.add(mergeTwoLists(lists.get(i), lists.get(i+1)));
                    i++;
                }else{
                    subLists.add(lists.get(i));
                }
            }
            return mergeK(subLists);
        }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }

        if(list1.val <= list2.val) {
            return new ListNode(list1.val, mergeTwoLists(list1.next, list2));
        } else {
            return new ListNode(list2.val ,mergeTwoLists(list1, list2.next));
        }
    }
}