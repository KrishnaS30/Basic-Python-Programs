#This program  either display the contents of a file or act as a simple calculator which stores the results into a file

#The following commands gets user selected option from the menu and stores in 'option' variable
print("calculator - To perform basic mathematical operations")
print("equation - To show all equations in the file")
option=input("Enter either 'calculator' or 'equation' from the menu above to proceed: ")
 
#The below loop is performed when user option is 'equation' to display contents of the file
while option=='equation':
    #The below commands get the file name from user, open and displays all the contents in the file and close the file
    try:
        filename=input("Enter the filename: ")
        f = open(filename +".txt", "r")
        print("\nThe file " + filename + ".txt contains: \n")
        print(f.read())
        f.close()
        break
    #The following commands displays an error message if the user entered file name is not found in the directory and prompt user to try entering again
    except FileNotFoundError:
        print("The entered file does not exist. Please try again")
        continue
    
#The below loop act as a simple calculator and is performed when user option is 'calculator'
while option=='calculator':
    #The below commands asks user to input two numbers and stores them
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
    #The below commands displays error message if user has entered non-numeric value and prompt user to enter input again
    except ValueError:
        print("That was not a valid number. Try again..")
        continue
    #The below command asks user to enter the operator and stores in 'operator' variable
    operator=input("Enter the operation(+,-,*,/): ")
    #The below loop checks 'operator' variable, perform operations accordingly and stores the answer in 'result' variable
    if operator == '+':
        result=num1+num2
    elif operator == '-':
        result=num1-num2
    elif operator =='*':
        result= num1*num2
    elif operator == '/':
        try: 
            result =num1/num2
        #The following command displays an error message when the user input second number is 0 and operator is '/', also prompt user to enter values again
        except ZeroDivisionError:
            print("Division by zero is not possible. Try again..")
            continue
    #The below command prints error message when an invalid operator is entered by user and prompt user to try again
    else:
        print("Not a valid operator. Try again..")
        continue
    #The below command displays the result
    print("The result is: ", result)
    #The following command stores complete equation in proper format to 'expression' variable
    expression="{}{}{}{}{}".format(num1,operator,num2," = ",result)
    
    #The below commands opens the 'expressions.txt' file and appends the 'expression' to the file
    #file=None
    try:   
        file=open('expressions.txt','a')
        file.write(expression)
        file.write('\n')
        print("Equation " + expression + " is saved to the file")
    #The following command displays an error message if the file is not found in the directory
    except FileNotFoundError:
        print("The file that you are trying to open does not exist")
    #The following command is used to close the opened file 
    finally:
        if file is not None:
            file.close()
    break
#When user option is neither 'equation' nor 'calculator' the following command outputs an error message
else:
    print("Selected option is not valid")



