#
#   Question: Write a function that computes the max profit that can be 
#   made by buying and then selling a single share TWICE. The second purchase
#   must be made on another date after the first sale
#

def buy_sell_stock_twice(A):
    
    first_buy_sell_profits = [0] * len(A)
    min_price_so_far = float('inf')
    max_profit = 0

    # Forward phase:
    # for each day, record the max profit if we sell
    # on that day. record it in first_buy_sell_profits
    for i in range(len(A)):
        min_price_so_far = min(min_price_so_far, A[i])
        max_profit = max(max_profit,A[i] - min_price_so_far)
        first_buy_sell_profits[i] = max_profit
    
    # Backwards phase:
    # For each day, find the max profit if we make
    # the second purchase on that day
    max_price_so_far = float('-inf')
    for i,price in reversed(list(enumerate(A[1:],1))):
        max_price_so_far = max(max_price_so_far,price)
        max_profit = max(max_profit, (max_price_so_far - price) + first_buy_sell_profits[i-1])

    return max_profit

# time complexity: O(n)
# space complexity: O(n)




