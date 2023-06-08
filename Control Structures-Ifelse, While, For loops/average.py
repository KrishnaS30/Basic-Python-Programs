# This program calculates the average of entered numbers until -1 is entered by user

#The below commands initializes 'count' and 'sum' variable to '0' value
count=0
sum=0
#The following command is a loop which gets user input and calculates the sum of numbers and count until user enters -1
while True:
    number = float(input("Enter a number(Enter -1 to stop entering numbers): "))
    #The below commands checks if user has entered -1 and if yes, exits the loop
    if number ==-1:
        break
    #The below commands increases the count and calculates the sum of numbers entered
    else:
        count+=1
        sum+=number
#The following commands calculates the average of numbers inputted and displays the result
print("The average of entered numbers(excluding -1) is : " , sum/count)

