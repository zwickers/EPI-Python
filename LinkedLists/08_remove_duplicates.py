#
#   Question: Write a function that removes
#   duplicates from a sorted Linked List,
#   and returns the head of the Linked List
#

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# Time complexity: O(n)
# Space complexity: O(1)
def remove_duplicates(head):
    node = head
    while node and node.next:
        # Because the input list is sorted,
        # you can determine if a node is a duplicate 
        # by comparing its value to the node after it in the list. 
        if node.data == node.next.data:
             # if it is, "skip" the next node
             # by changing the next pointer
             # and let garbage collection take care of it
            node.next = node.next.next
        else:
            # otherwise, keep traversing the linked list
            node = node.next
    return head




