def max_profit_two_transactions(prices):
    n = len(prices)
    if n < 2:
        return 0

    # Initialize the profit arrays
    first_buy = float('-inf')
    first_sell = 0
    second_buy = float('-inf')
    second_sell = 0

    for price in prices:
        # First transaction: buy or hold
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, first_buy + price)

        # Second transaction: buy or hold
        second_buy = max(second_buy, first_sell - price)
        second_sell = max(second_sell, second_buy + price)

    return second_sell