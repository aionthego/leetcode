from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        if not l1 and not l2:
            return result
        elif not l1 or not l2:
            result = l1 or l2    
        else:
            carry = 0
            res = ListNode(0, None)
            sentinel = res
            while l1 or l2:
                sum = carry
                if l1:
                    sum += l1.val
                    l1 = l1.next
                if l2:
                    sum += l2.val
                    l2 = l2.next
                res.next = ListNode(sum % 10, None)
                res = res.next
                carry = sum // 10
            if carry > 0:
                res.next = ListNode(carry, None)
            result = sentinel.next
            del sentinel

        return result

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2,ListNode(4,ListNode(3,None)))
    l2 = ListNode(5,ListNode(6,ListNode(4,None)))
    #expected result = ListNode(7,ListNode(0,ListNode(8,None)))
    result = s.addTwoNumbers(None,None)
    print(result.val)
    result = s.addTwoNumbers(l1,None)
    print(result.val)
    result = s.addTwoNumbers(None,l2)
    print(result.val)
    result = s.addTwoNumbers(l1,l2)
    while result:
        print(result.val)
        result = result.next
    

