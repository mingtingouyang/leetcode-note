# Add Two Numbers

## 题目

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

> 输入：l1 = [2,4,3], l2 = [5,6,4]\
> 输出：[7,0,8]\
> 解释：342 + 465 = 807.

**示例 2：**

> 输入：l1 = [0], l2 = [0]\
> 输出：[0]

**示例 3：**

> 输入：l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]\
> 输出：[8, 9, 9, 9, 0, 0, 0, 1]

**提示：**

- 每个链表中的节点数在范围 [1, 100] 内
- 0 <= Node.val <= 9
- 题目数据保证列表表示的数字不含前导零

## 解题思路

### 方案 1

由于链表是逆序存储数字的位数的，因次可以同时遍历两个列表，同时出现的数字相加存储在输出的链表里即可。只需要做好进位的处理。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        carry = False
        result_cur = result

        while None != l1 or None != l2 or carry:
            val = 0
            if None != l1:
                val += l1.val
                l1 = l1.next
            if None != l2:
                val += l2.val
                l2 = l2.next
            if carry:
                val += 1
                carry = False
            if val > 9:
                val -= 10
                carry = True

            node = ListNode(val=val)
            result_cur.next = node
            result_cur = node
        
        return result.next
```
