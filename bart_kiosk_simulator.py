#This program simulates the BART Kiosk!
#CONSTANTS
DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.80
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

def load_card(num_ones, num_fives, num_tens, num_twenties):
	return (num_ones * 1) + (num_fives * 5) + (num_tens * 10) + (num_twenties * 20)

print load_card(0, 0, 0, 0)
print load_card(0, 0, 0, 9)
print load_card(2, 3, 0, 0)
print load_card(3, 1, 1, 3)

def travel_to_destination(fare_price, card_value):
	if fare_price <= card_value:
		print "Welcome aboard, enjoy your trip!"
	if fare_price >= card_value:
		print "You need more money!"

clipper_card1 = load_card(3, 0, 0, 0)

travel_to_destination(FREMONT_TO_COLMA, clipper_card1)

clipper_card2 = load_card(0, 0, 0, 1)

travel_to_destination(HAYWARD_TO_CONCORD, clipper_card2)

clipper_card3 = load_card(1, 1, 0, 0)

travel_to_destination(DUBLIN_TO_POWELL, clipper_card3)

clipper_card4 = load_card(2, 0, 1, 0)

travel_to_destination(FRUITVALE_TO_UNION_CITY, clipper_card4)

