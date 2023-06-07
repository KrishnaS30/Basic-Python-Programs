#This program produces '*' pyramid pattern

#The below nested for loops produces the '*' pyramid pattern 
#'i' represents rows-changes value from 1 to 5 and 'j' represents columns-changes from 0 to i-1
for i in range(1,6):
    for j in range(0,i):
        #The below commands prints the '*' in the same line
        print('*',end="")
    #The below command gives a newline after each row is displayed
    print("")
    