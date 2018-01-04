#
#   Question: A 64-bit integer could be viewed as an array of bits, where the 0th
#   index is the LSB, and the 63rd index is the MSB. Given an integer and two
#   indices, i and j, swap the two bits at i and j.
#

def swap_bits(num,i,j):

    # check if the i-th and j-th bits differ
    if (num >> i) & 1 != (num >> j) & 1:
        # we can swap the i-th and j-th bits by
        # simply flipping their values

        # select the bits that must be flipped
        bit_mask = (1 << i) | (1 << j)
        
        # x ^ 1 should be 1 when x = 0 and should be 0 when x = 1
        # so the flip should be performed with an XOR
        num = num ^ bit_mask

    return num
   
   
# Time complexity: O(1)
