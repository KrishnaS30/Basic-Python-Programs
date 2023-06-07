#This program checks whether user has entered their full name

#The following command gets the full name entered by user and stores in 'full_name' variable
full_name=input("Enter your full name: ")

#The below commands check for different conditions for a valid full name and displays the message
if len(full_name)==0:
    print("You haven't entered anything")
elif len(full_name)<4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name)>25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else: 
    print("Thankyou for entering your name.")