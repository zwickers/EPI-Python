#
#   Question: Write a function that deletes a node in
#   a singly linked list. The input node is guaranteed not 
#   to be the tail node.
#

class ListNode:
    def __init__(self,data,next):
        self.data = data
        self.next = next

# Time complexity: O(1)
def(node_to_delete):
    # copy the next node's value
    node_to_delete.data = node_to_delete.next.data
    # update the current node's next pointer to skip the next node
    node_to_delete.next = node_to_delete.next.next
