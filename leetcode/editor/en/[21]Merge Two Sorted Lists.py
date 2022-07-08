# You are given the heads of two sorted linked lists list1 and list2. 
# 
#  Merge the two lists in a one sorted list. The list should be made by 
# splicing together the nodes of the first two lists. 
# 
#  Return the head of the merged linked list. 
# 
#  
#  Example 1: 
# 
#  
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#  
# 
#  Example 2: 
# 
#  
# Input: list1 = [], list2 = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both lists is in the range [0, 50]. 
#  -100 <= Node.val <= 100 
#  Both list1 and list2 are sorted in non-decreasing order. 
#  
#  Related Topics Linked List Recursion 👍 13198 👎 1193


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = tmp = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tmp.next = list1
                list1, tmp = list1.next, list1
            else:
                tmp.next = list2
                list2, tmp = list2.next, list2
        if list1 or list2:
            tmp.next = list1 if list1 else list2
        return list.next


# leetcode submit region end(Prohibit modification and deletion)

e = Solution()

d = ListNode(5, None)
c = ListNode(4, d)
b = ListNode(3, c)
a = ListNode(2, b)

x = ListNode(6, None)
y = ListNode(4, x)
z = ListNode(2, y)

res = e.mergeTwoLists(a, z)
while res is not None:
    print(res.val)
    res = res.next
