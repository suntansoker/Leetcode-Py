'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        st2 = []

        while l1 and l2:
            st1.append(l1.val)
            st2.append(l2.val)
            l1 = l1.next
            l2 = l2.next

        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry = 0
        st = []
        while st1 and st2:
            val = st1.pop() + st2.pop() + carry
            carry = val // 10
            sm = val % 10
            st.append(sm)

        while len(st1) > 0:
            val = st1.pop() + carry
            carry = val // 10
            sm = val % 10
            st.append(sm)

        while len(st2) > 0:
            val = st2.pop() + carry
            carry = val // 10
            sm = val % 10
            st.append(sm)

        if carry > 0:
            st.append(carry)

        head = ListNode()

        tmp = head

        while (st):
            tmp.next = ListNode(st.pop())
            tmp = tmp.next

        return head.next
