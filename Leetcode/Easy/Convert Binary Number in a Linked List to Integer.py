# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# def getDecimalValue(head):
#     a,p = 0,0
#     for i in head[::-1]:
#         a += i * (2**p)
#         p += 1
#     return a


# def getDecimalValue(head):
#     return int(''.join(map(str,head)),2)


# Правильное решение, там связанные списки
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ''
        while True:
            res += str(head.val)
            if head.next == None:
                break
            head = head.next
        return int(res,2)

print(Solution.getDecimalValue([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]))
