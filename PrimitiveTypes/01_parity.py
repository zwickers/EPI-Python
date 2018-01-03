#
#   Question: Find the parity of a 64 bit number.
#             Return a 1 if odd number of 1-bits, or a 0 if an even number of 1-bits.
#

# Brute force solution
# O(n) runtime: count the number of 1-bits, and check if it is even
def parity(num):
    counter = 0
    while num:
        counter += num & 1
        num >>= 1
    return counter % 2

# Slightly optimizied solution:
# This solution takes advantage of the fact that x & (x-1) is equal to x with it's lowest 1-bit erased
# O(k) runtime, where k is the number of 1-bits
def parity(num):
    result = 0
    while num:
        result ^= 1
        num = num & (num - 1)
    return result

# When you XOR all the bits together, if the number of bits with the value 1 is odd,
# then you will be left with a 1.
# This solution takes advantage of that fact that XOR is associative,
# in other words, it doesn't matter what order you XOR the bits in, you
# will get the same result. Therefore we can use a binary-partition scheme to
# achieve O(log n) time complexity.
# NOTE: assumes the input is a 64 bit integer
def parity(num):
    num ^= num >> 32 # xor first and second half, ignore 1st half
    num ^= num >> 16 
    num ^= num >> 8
    num ^= num >> 4
    num ^= num >> 2
    num ^= num >> 1
    return num & 1 # extract out the last bit
