#
#   Question: Write a function that takes as input a sorted array and updates
#   it so that all duplicates have been removed and the remaining elements
#   have been shifted left to fill the emptied indices. Return the number
#   of valid indices. Do this IN PLACE, using no extra memory/hashtables etc.
#


# Time complexity: O(n)
# Space complexity: O(1)
def delete_duplicates(A):
    # just return 0 for an empty array
    if not A:
        return 0
    
    write_index = 1

    for i in range(1,len(A)):
        if A[write_index-1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    
    # 0 out the rest of the array
    for i in range(write_index,len(A)):
        A[i] = 0

    return write_index
