#
#   Question: Write a function that takes as input a list denoting 
#   the daily stock price, and returns the maximum profit that could
#   be made by buying and then selling one share of that stock
#

# Compute the difference of the current price entry with the minimum price seen
# so far as we iterate through the list
# time complexity: O(n), where n is the length of the array
# space complexity: O(1)
def buy_sell_stock_once(A):
    min_price_so_far = float('inf')
    max_profit = float('-inf') 
    for i in range(len(A)):
        if A[i] < min_price_so_far:
            min_price_so_far = A[i]
        max_profit = max(max_profit, A[i] - min_price_so_far) 
    return max_profit
    
    
    
    
    
    
    
    
    
