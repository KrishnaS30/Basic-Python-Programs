#This program prints sentence after applying string manipulations

#Below command stores the string
sentence= "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#The below command replaces the '!' in a string with blank space
replaced_sentence=sentence.replace("!", " ")

#The following commands displays the proper sentence, sentence in upper case and the sentence reversed
print(replaced_sentence)
print(replaced_sentence.upper())
print(replaced_sentence[::-1])