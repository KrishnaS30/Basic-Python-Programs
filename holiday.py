#This program gives a price deal for holiday package to one of the 4 cities in UK which includes the flight cost, hotel cost and car rental cost based on user inputs-destination city, number of nights to stay at hotel and number of days to hire a car

#The following commands displays the headline and 4 UK city options for the holiday
print("Explore UK cities with ABC Holidays!! Check our low price deals!!")
print("Belfast, Bristol, Cardiff, Norwich")
#The below command creates a list which contains the 4 UK cities in all lowercase letters and stores it in variable 'city_list'
city_list=['belfast', 'bristol', 'cardiff', 'norwich']
#The below loop is performed to get appropriate user input and displays an error message when invalid input is entered
#'city_flight'- variable to store the city entered by user. The user entered city(converted to all lowercase) is checked whether it belongs to the list- 'city_list', if not, displays error message and prompt user to enter city again
#'num_nights' and 'rental_days' are variables to store the no. of nights for hotel stay and no. of days for car hire respectively. If user enters a non-numeric input for these, error message is displayed and prompt user to enter the value again
while True:
    city_flight=input("Choose your holiday destination from above options: ")
    if city_flight.lower() in city_list:
        while True:
            try: 
                num_nights=int(input("Enter the number of nights for staying at hotel: "))
                break
            except ValueError:
                print("You have entered an invalid number. Please try again..")
                continue
        while True:       
            try:
                rental_days=int(input("Enter the number of days for hiring a car: "))
                break
            except ValueError:
                print("You have entered an invalid number. Please try again..")
                continue
        break
    else:
        print("Sorry! Currently we have no deals to the entered city. Please try again..")
        continue
# The below function calculates, returns and displays the total cost of hotel for the number of nights provided by the user
def hotel_cost(num_nights):
    price_per_night=200.0
    cost_hotel=num_nights*price_per_night
    print("The total cost of hotel stay for {} nights : {}".format(num_nights, cost_hotel))
    return cost_hotel

#The below function checks the destination city, returns and displays the cost of flight for the city provided by the user
def plane_cost(city_flight):
    if city_flight.lower() == 'cardiff':
        cost_flight=100.0
    elif city_flight.lower() =='bristol':
        cost_flight=60.0
    elif city_flight.lower() =='belfast':
        cost_flight=90.0
    elif city_flight.lower() =='norwich':
        cost_flight=250.0
    print("\nThe flight cost to {} : {}".format(city_flight.upper(), cost_flight))
    return cost_flight
 
#The below function calculates, returns and displays the total car rental cost for the number of days provided by the user  
def car_rental(rental_days):
    rent_per_day=40.0
    cost_car_rental=rental_days*rent_per_day
    print("The total cost of hiring a car for {} days : {}".format(rental_days, cost_car_rental))
    return cost_car_rental

#The below function takes in three parameters-'hotel','plane','car' which contains the cost returned by respective functions, calculates and returns the total cost for the holiday
def holiday_cost(hotel,plane,car):
    total_cost_holiday=plane(city_flight)+hotel(num_nights)+car(rental_days)
    return total_cost_holiday

#The below command calls the 'holiday_cost' function with the other three functions as arguments and stores the returned total cost in the variable 'final_cost' 
final_cost=holiday_cost(hotel_cost,plane_cost,car_rental)
#The below command displays the total cost for the holiday
print("HOORAY!! Price deal for a holiday to {} is just {}\n".format(city_flight.upper(),final_cost))




