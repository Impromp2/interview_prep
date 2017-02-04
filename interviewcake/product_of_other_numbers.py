# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

# def get_products_of_all_ints_except_at_index(int_list):
# 	new_list = []

#   	products_of_all_ints_before_index = [None] * len(int_list)

# 	# for each integer, find the product of all the integers
# 	# before it, storing the total product so far each time
# 	product_so_far = 1
# 	for i in range(len(int_list)):
# 	    products_of_all_ints_before_index[i] = product_so_far
# 	    product_so_far *= int_list[i]

# 	products_of_all_ints_after_index = [None] * len(int_list)

# 	product_so_far = 1
# 	i = len(int_list) - 1
# 	while i >= 0:
# 	    products_of_all_ints_after_index[i] = product_so_far
# 	    product_so_far *= int_list[i]
# 	    i -= 1


def get_products_of_all_ints_except_at_index(int_list):
	new_list = [None] * len(int_list)

	product_so_far = 1
	for i in range(len(int_list)):
	    new_list[i] = product_so_far
	    product_so_far *= int_list[i]

	product_so_far = 1
	i = len(int_list) - 1
	while i >= 0:
	    new_list[i] = product_so_far * new_list[i]
	    product_so_far *= int_list[i]
	    i -= 1

	print(new_list)


get_products_of_all_ints_except_at_index([2,4,0])