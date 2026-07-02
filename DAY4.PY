#REVERSE LINKED LIST
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None 
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr     
            curr = temp      
            
        return prev
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    sol = Solution()
    reversed_head = sol.reverseList(head)
    current = reversed_head
    output = []
    while current:
        output.append(str(current.val))
        current = current.next
    
    print(" -> ".join(output))
    
    
#MERGE TWO SORTED LISTS


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution: 
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode: 
        dummy = ListNode(0) 
        current = dummy 
        while list1 and list2: 
            if list1.val <= list2.val: 
                current.next = list1 
                list1 = list1.next 
            else: 
                current.next = list2 
                list2 = list2.next 
            current = current.next 
        current.next = list1 or list2 
        return dummy.next
def to_linked_list(iterable):
    """Converts a standard Python list into a ListNode linked list."""
    dummy = ListNode(0)
    current = dummy
    for val in iterable:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Prints the linked list values in a readable format."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "Empty List")

input_list1 = [1, 2, 4]
input_list2 = [1, 3, 4]
list1 = to_linked_list(input_list1)
list2 = to_linked_list(input_list2)
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)
print("Merged Output:")
print_linked_list(merged_head)
 


#add two numbers

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode() 
        res = dummy 
        total = carry = 0 
        while l1 or l2 or carry: 
            total = carry 
            if l1: 
                total += l1.val 
                l1 = l1.next 
            if l2: 
                total += l2.val 
                l2 = l2.next 
            num = total % 10 
            carry = total // 10 
            dummy.next = ListNode(num) 
            dummy = dummy.next 
        return res.next


def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))

l1 = build_linked_list([2, 4, 3])
l2 = build_linked_list([5, 6, 4])

solution = Solution()
output_node = solution.addTwoNumbers(l1, l2)
print("Result Linked List:")
print_linked_list(output_node)
