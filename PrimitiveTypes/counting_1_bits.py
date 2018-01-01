#
# Problem: Count the number of 1 bits in an integer
#

def count_bits(num):
    one_bits = 0
    while num:
        # if the least significant bit (LSB) is 1, increment the value of one_bits
        one_bits += num & 1
        # perform a right bitshift
        num >>= 1
    return one_bits
        
# Time Complexity: O(n)
# Explanation: We perform an O(1) operation per bit, so the time complexity must be O(n), 
# where n is the number of bits needed to represent the integer (Ex: 4 bits are needed
# to represent the number 12: 1100)
