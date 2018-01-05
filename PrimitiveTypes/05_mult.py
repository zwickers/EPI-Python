#
#   Question: Sometimes the processors used in ultra low-power devices such as hearing aids
#   do not have dedicated hardware for performing multiplication. Write a function that
#   multiplies two non-negative integers ** WITHOUT USING ARITHMETICAL OPERATORS **.
#   You are only allowed to use assignment, bitwise operators, and boolean operators/equality checks.
#

# uses half-adder circuit logic to add two numbers
# sum = a ^ b
# carry = a & b
def add(a,b):
    while b:
        # carry now contains common set bits of x and y
        carry = a & b 
        # sum of bits of x and y where at least one of the bits is not set
        a = a ^ b 
        # carry is shifted to the left by one so that adding it to a gives the required sum
        b = carry << 1
    return a

# using the Egyption multiplication algorithm
# https://mindyourdecisions.com/blog/2014/08/27/the-egyptian-method-russian-peasant-multiplication-video-and-a-proof/#.U_5I5vldV8E
def multiply(a,b):
    running_sum = 0
    while b:
        if b & 1: 
            result = add(result,a) #if b is odd, add a to result
        a <<= 1 # a = a*2
        b >>= 1 
    return running_sum

# time complexity: O(n^2)
    # The time complexity of addition is O(n), where n is the number of bits needed to represent
    # the operands. Since we do up to n additions to perform a single multiplication, the total
    # time complexity is O(n^2)
