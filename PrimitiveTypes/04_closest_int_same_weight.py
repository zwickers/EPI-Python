#
#   Question: FIND THE CLOSEST INTEGER WITH THE SAME WEIGHT
#   Define the weight of a non-negative integer x as the number of bits
#   in x that are set to 1 in it's binary representation. For example,
#   since 92 in binary is 1011100, the weight of 92 is 4.
#   Write a method which takes as input a non-negative integer x and
#   returns a number y which is not equal to x, but has the same weight as x,
#   and their difference, |x - y|, is as small as possible. You can assume x is
#   not 0 or all 1s.
#  

# the linear time approach is to swap the two rightmost consecutive bits that are different
# time complexity: O(n), where n is the number of bits in the integer
def closest_int_same_weight(x):
    NUM_UNSIGNED_BITS = 64     # assume the integer is 64-bit
    for i in range(0,NUM_UNSIGNED_BITS):
        if (x >> i) & 1 != (x >> (i + 1)) & 1: # check if two consecutive bits are different
            bit_mask = (1 << i) | (1 << (i + 1))
            result = x ^ bit_mask
            return result
    #if all bits are 0 or 1, raise an error
    raise ValueError('All bits are 0 or 1!')        


