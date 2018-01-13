#
#   Question: Consider two singly Linked Lists
#   in which each node holds a number. Assume each
#   list is sorted in ascending order within each list.
#   The merge of the two lists is a list consisting of the
#   nodes of the two lists in which numbers appear in ascending order
#   Write a function takes in two such lists and returns their merge.
#

class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

# Time complexity: Time complexity : O(n+m) where n is the number of
# nodes in the first list, and m is the number of nodes in the second list
# Space complexity: O(1) because we just use the existing nodes
def merge_two_sorted_lists(head1, head2):
    
    dummy_head = tail = ListNode()

    while head1 and head2:
        if head1 < head2:
            tail.next = head1
            head1 = head1.next
        else: # head2 < head1
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # append the remaining list 
    tail.next = L1 or L2

    return dummy_head.next

    
