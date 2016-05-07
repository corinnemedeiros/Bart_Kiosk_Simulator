def load_card(num_ones, num_fives, num_tens, num_twenties):
	return (num_ones * 1) + (num_fives * 5) + (num_tens * 10) + (num_twenties * 20)

print load_card(0, 0, 0, 0)
print load_card(0, 0, 0, 9)
print load_card(2, 3, 0, 0)
print load_card(3, 1, 1, 3)
