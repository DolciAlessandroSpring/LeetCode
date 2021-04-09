
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        p = []
        obj = self
        while(obj != None):
            p.append(obj.val)
            obj = obj.next
        return str(p)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def fill_value(l1: ListNode, l2: ListNode, residual = 0):
            
            # Fix cases where l1 and l2 have different lengths
            if ((l1 == None) & (l2 != None)):
                l1 = ListNode()
            elif ((l1 != None) & (l2 == None)):
                l2 = ListNode()
            
            # Main case
            if ( (l1 != None) | (l2 != None)):
                
                # Sum and residual
                s = l1.val + l2.val + residual
                res = s // 10
                        
                l1 = l1.next
                l2 = l2.next
                l3 = ListNode(val = s % 10,
                              next = fill_value(l1, l2, residual = res))
            else:
                
                # The last digit can still be the residual from the previous step
                if residual == 0:
                    l3 = None
                else:
                    l3 = ListNode(val = residual)
            
            return l3
        
        result = fill_value(l1, l2, residual = 0)
        print("The result is: ", result)
        
        return result


##########################  TEST  ##########################

# Function to generate an array from input
def generate_array():
    n = int(input("Enter number of elements: "))
    lst = []
    for i in range(0, n):
        lst.append(int(input("Type a digit: ")))
    print(lst)
    return lst


# Function to transform a list into a ListNode
def list2link(l):
    if len(l) == 0:
        return None
    ret_tail = ret_head = ListNode(l[0])
    for val in l[1:]:
        tmp = ListNode(val)
        ret_tail.next = tmp
        ret_tail = ret_tail.next
    return ret_head


a1 = list2link(generate_array())
a2 = list2link(generate_array())

result = Solution().addTwoNumbers(a1, a2)
