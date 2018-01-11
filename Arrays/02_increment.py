#
#   Question: Write a function that takes as input an array of digits encoding a decimal integer D
#   and updates the array to represent the integer D + 1. Your algorithm should work even if it
#   is implemented in a language that has finite-precision arithmetic.
#

# Time complexity: O(n), where n is the length of A. 
def increment(A):
    i = len(A) - 1
    if A[i] < 9:
        A[i] += 1
    else:
        # during the stretch of 9's, keep setting the individual element to 0,
        # until you reach an element that is not 9, then increment that element
        while A[i] == 9:
            # handles the edge case where the entire array is all 9's
            if i == 0:
                A[i] = 0
                A.insert(0,1)
                return
            A[i] = 0
            i -= 1
        A[i] += 1
