# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

def highest_prod(intlist)
	if intlist.length < 3
		return
	end

	highest = [intlist[0], intlist[1]].max
	lowest = [intlist[0], intlist[1]].min

	highest_prod_of_2 = highest * lowest
	lowest_prod_of_2 = highest * lowest

	highest_prod_of_3 = intlist[0] * intlist[1] * intlist[2]

	intlist.each_with_index do |value, i|
		# we have already done calculations for first two values
    if i < 2
			next
		end

		highest_prod_of_3 = [
			highest_prod_of_3,
			highest_prod_of_2 * value,
			lowest_prod_of_2 * value
		].max

		highest_prod_of_2 = [
			highest_prod_of_2,
			lowest * value,
			highest * value
		].max

		lowest_prod_of_2 = [
			lowest_prod_of_2,
			lowest * value,
			highest * value
		].min

		highest = [
			highest,
			value
		].max

		lowest = [
			lowest,
			value
		].min
	end

	return highest_prod_of_3
end

intlist = [-10,5,10,-39,40]
puts highest_prod(intlist)