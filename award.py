#This program displays the award received for triathlon based on the total time taken by the contestent

#The following commands gets the contestent's time taken for three sports events
swimming_time=float(input("Enter the time taken for swimming(in minutes): "))
cycling_time=float(input("Enter the time taken for cycling(in minutes): "))
running_time=float(input("Enter the time taken for running(in minutes): "))

#The following command gets the qualifying total time for the triathlon
qualifying_time=100.0

#The below commands calculates and prints the total time taken by contestent to complete triathlon
total_time_taken=swimming_time+cycling_time+running_time
print("Total time taken to complete the triathlon is " + str(total_time_taken))

#The below commands checks the total time taken and prints the award received
if total_time_taken<=qualifying_time:
    print("Congratulations! You have received Provincial Colours Award")
elif qualifying_time<total_time_taken<=(qualifying_time+5.0):
    print("Congratulations! You have received Provincial Half Colours Award")
elif (qualifying_time+5.0)<total_time_taken<=(qualifying_time+10.0):
     print("Congratulations! You have received Provincial Scroll Award")
else:
     print("You are not qualified. Best of luck next time!")