#
#   Question: Write a program that takes an array A and an index i,
#   and rearranges the elements such that all elements less than A[i] (the pivot)
#   appear first, followed by elements equal to the pivot, followed by elements
#   greater than the pivot
#

def dutch_flag_partitioning(A,pivot_index):
    pivot = A[pivot_index]
    less,greater = 0,len(A)-1
    i = 0
    # less than pivot:    A[:less]
    # equal to pivot:     A[less:greater]
    # greater than pivot: A[greater:]
    # unclassified:       A[i:greater]

    while i <= greater:
        # A[i] is the incoming unclassified element
        if A[i] < pivot:
            A[i], A[less] = A[less], A[i]
            i += 1
            less += 1
        elif A[i] == pivot:
            i += 1
        else: # A[i] > pivot
            A[i],A[greater], A[greater], A[i]
            greater -= 1

# each iteration decreases the size of unclassified by 1, and the time spent on each
# iteration is O(1), so the time complexity is O(n)
# since this is solved in-place, the space complexity is O(1)
