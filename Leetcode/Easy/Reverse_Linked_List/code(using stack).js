/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var stack = [];
    current = head;
    while(current != null){
        stack.push(current.val);
        current = current.next;
        head = current;
    } 
    head = null;
    if(stack.length != 0){
        newNode = new ListNode(stack[stack.length -1], null);
        head = newNode;
        stack.pop();
        current = head;
        while( stack.length != 0){
            newNode = new ListNode(stack[stack.length -1], null);
            current.next = newNode;
            current = current.next;
            stack.pop();
        }
    }
    return head;

};