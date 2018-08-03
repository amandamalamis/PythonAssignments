# Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() method to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__(), also write the code so that the initial miles is set to be 0 whenever a new instance is created.

# Add the following methods to this class:

# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?

class Bike:
    def __init__(number, price, max_speed, miles):
        number.price = price
        number.max_speed = max_speed
        number.miles= miles

    def displayInfo(number):
        print("Price " + str(number.price))
        print("Maximum Speed " + str(number.max_speed))
        print("Mileage " + str(number.miles))
        return number

    def ride(number):
        number.miles= number.miles + 10
        print("Riding", number.miles)
        return number

    def reverse(number):
        number.miles= number.miles-5
        print("Reverse", number.miles)
        return number

bikeA = Bike("$1,000", "4,000", 100)
bikeA.displayInfo()

while True:
    x = input("Ride, Reverse, or Exit?")
    if ((x == "Ride") or (x == "ride")):
        bikeA.ride()
        continue

    if ((x == "Reverse") or (x == "reverse")):
        bikeA.reverse()
        continue