# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Solution 1
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


if __name__ == "__main__":
    # first list
    l1_3 = ListNode(val=3)
    l1_2 = ListNode(val=4, next=l1_3)
    l1_1 = ListNode(val=2, next=l1_2)
    
    # second list
    l2_3 = ListNode(val=4)
    l2_2 = ListNode(val=6, next=l2_3)
    l2_1 = ListNode(val=5, next=l2_2)

    solution = Solution()
    res = solution.addTwoNumbers(l1=l1_1, l2=l2_1)
    while None != res:
        print(res.val)
        res = res.next