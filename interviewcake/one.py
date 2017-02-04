# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [10,9,8,7,5]

def get_max_profit(stock_prices_yesterday):
	max_profit = None

	for x in range(len(stock_prices_yesterday)):
		buy_price = stock_prices_yesterday[x]
		for y in range(len(stock_prices_yesterday[x:])):
			sell_price = stock_prices_yesterday[x+y]

			if buy_price < sell_price and sell_price - buy_price > max_profit:
				max_profit = sell_price - buy_price

	print max_profit


get_max_profit(stock_prices_yesterday)



def get_max_2(stock_prices_yesterday):
	max_profit = 0
	buy_price = 0
	sell_price = 0

	for x in range(len(stock_prices_yesterday)):
		if x == 0:
			buy_price = stock_prices_yesterday[x]
		else:
			if stock_prices_yesterday[x] < buy_price:
				buy_price = stock_prices_yesterday[x]
			elif stock_prices_yesterday[x] >= buy_price and stock_prices_yesterday[x] - buy_price > max_profit:
				sell_price = stock_prices_yesterday[x]
				max_profit = sell_price - buy_price

	print max_profit

get_max_2(stock_prices_yesterday)