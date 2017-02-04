# Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was
# 9:30am local time.

# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns
# the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

stock_prices_yesterday = [101, 115, 99, 110, 107, 105]

def get_max_profit(stock_prices_yesterday):
	max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
	buy_price = stock_prices_yesterday[0]

	for x in range(len(stock_prices_yesterday)):
		if len(stock_prices_yesterday) < 2:
			raise IndexError('Need at least 2 prices to buy and sell!')

		# have to buy before you can sell, so first iteration you must buy.
		if x > 0:
			current_profit = stock_prices_yesterday[x] - buy_price
			max_profit = max(current_profit, max_profit)
			buy_price = min(buy_price, stock_prices_yesterday[x])

	return max_profit

def main():
    max_profit = get_max_profit(stock_prices_yesterday)
    print(max_profit)

if __name__ == '__main__':
    main()
    
