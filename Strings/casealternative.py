# This program makes alternative upper and lower case characters or words based on the user selected option

#The following commands gets user selected option from the menu and stores in 'option' variable
print("character - To make each alternative character upper and lower case")
print("word - To make each  alternative word upper and lower case")
option=input("Enter an option from the menu: ")
#The below command converts the user option to all lowercase
option.lower()
#The below loop is performed when user option is 'character' - to display alternative characters in the string with different cases
if option=="character":
    #The following commands prompt user to enter a string and stores the string in 'original_string' variable and displays the string 
    original_string = input("Enter a string: ")
    print("The original string: ", original_string) 
    #The below command initializes an empty string
    alternative_string=str()
    #The below for loop generates the modified string
    #'char_index' represents the position of each character in the string and and the last position or range is determined using the length of the user entered string
    for char_index in range(len(original_string)):
        #The below loop checks the position of the character for even and modifies the 'alternative_string' variable accordingly
        if char_index%2==0:
            #If true,The character at 'char_index' position is changed to uppercase and added to the 'alternative_string' variable
            alternative_string=alternative_string+original_string[char_index].upper()
        else:
             #Otherwise,The character at 'char_index' position is changed to lowercase and added to the 'alternative_string' variable
            alternative_string= alternative_string+original_string[char_index].lower()
    #The below command displays the modified output string        
    print("The modified string: ",alternative_string)

#The below loop is performed when user option is 'word' - to display alternative words in the string with different cases
elif option=="word":
    #The following commands prompt user to enter a string and stores the string in 'original_string' variable and displays the string 
    original_string = input("Enter a string: ")
    print("The original string: ", original_string)
    #The below command initializes an empty list
    alternative_word=[]
    #The below command splits the string into a words list by using the delimiter whitespace and stores in the 'words' variable
    words= original_string.split()
    #The below for loop generates the modified string
    #'word_index' represents the position of each word in the list, the last position or range is determined by the length of the words list
    for word_index in range(len(words)):
         #The below loop checks the position of the word for even and modifies the 'alternative_word' variable accordingly
        if word_index%2==0:
            #If true,The word at 'word_index' position is changed to lowercase and is added to the 'alternative_word' list
            alternative_word.append(words[word_index].lower())
        else:
            #Otherwise,The word at 'word_index' position is changed to uppercase and is added to the 'alternative_word' list
            alternative_word.append(words[word_index].upper())
    #The below command displays the modified output by joining the words list using whitespace
    print("The modified string: "," ".join(alternative_word))

#The below commands prints error message when an invalid option is given by user
else:
    print("You have entered an invalid option")


