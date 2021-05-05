# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        node = l1
        while node:
            num1.append(node.val)
            node = node.next
        node = l2
        while node:
            num2.append(node.val)
            node = node.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        total_size = len(num1) if len(num1) >= len(num2) else len(num2)
        if len(num1) < len(num2):
            for x in range(total_size - len(num1)):
                num1.append(0)
        elif len(num2) < len(num1):
            for x in range(total_size - len(num2)):
                num2.append(0)
        result = [ 0 ] * total_size
        for i in range(total_size):
            digit1 = num1[i]
            digit2 = num2[i]
            r_digit = digit1 + digit2
            result[i] = r_digit
            if i > 0 and result[i-1] > 9:
                result[i-1] %= 10
                result[i] += 1
        if result[-1] > 9:
            result[-1] %= 10
            result.append(1)
        final_list = head = ListNode(result.pop())
        while result:
            final_list.next = ListNode(result.pop())
            final_list = final_list.next
        return head
            