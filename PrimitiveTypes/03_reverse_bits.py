#
#   Question: Write a method that takes a 64-bit integer as input and 
#   outputs the 64-bit integer consisting of the bits of the input integer
#   in reverse order.
#


# integer is between 0 and 2^{n}-1
# key idea: if binary representation contains 1 at i-th position, add 2^{n-i-1} to a new integer
# time complexity: O(n), space: O(1) ... this is okay if not needed too many times, or if n is constantly varying
def reverse_bits(x,n):
    result = 0
    for i in range(0,n):
        if (x >> i) & 1 == 1:
            result += 2 ** (n - i - 1)
    return result
