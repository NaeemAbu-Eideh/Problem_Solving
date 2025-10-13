# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str_num1 = ""
        str_num2 = ""
        node1 = l1
        node2 = l2

        while node1 != None:
            str_num1 += str(node1.val)
            node1 = node1.next
        while node2 != None:
            str_num2 += str(node2.val)
            node2 = node2.next
        
        str_num1 = str_num1[::-1]
        str_num2 = str_num2[::-1]
        num = int(str_num1) + int(str_num2)
        str_num = str(num)
        str_num = str_num[::-1]
        l3 = ListNode(int(str_num[0]))
        l3.next = None
        length = len(str_num)
        head = l3
        for i in range(1, length):
            l = ListNode(int(str_num[i]))
            head.next = l
            head = l
        return l3

