#This program is 'Little Sister's Vocabulary' in Exercism which performs some major string transformations

"""Functions for creating, transforming, and adding prefixes to strings."""

#This function takes in a word and returns the new word after adding 'un' prefix to it
def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un"+word

#This function takes in a list of words containing a prefix as first element followed by some words and returns a string after adding the prefix to the words
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix_applied=vocab_words[0]
    for index in range(1,len(vocab_words)):
           prefix_applied=prefix_applied+" :: "+ vocab_words[0]+vocab_words[index]
    return prefix_applied


#This function takes in a word and returns a new word after removing the 'ness' suffix or if the suffix is 'iness', the word is appended with 'y'
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if "iness" in word:
        return word.replace("iness","y")
    return word.replace("ness","")
    

#This function takes in a sentence and an index position of the adjective in the sentence and returns the corresponding verb by adding 'en' suffix to the adjective
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """
    split_words=sentence.replace(".","").split()
    return split_words[index]+"en"

#This is the main function which is executed initially, it takes in user inputs, calls the functions and displays the corresponding returned strings
def main():

    #The below loop prompts user to input data, shows error message if user enters wrong data, calls function 'add_prefix_un' and displays the returned word
    while True:
        wordlist=['happy', 'manageable', 'fold', 'eaten', 'avoidable', 'usual']
        print("Enter any word from the options below inorder to add prefix 'un' \n", wordlist)
        word=input().lower()
        if word in wordlist:
            print("Adding prefix 'un' to the word gives: ",add_prefix_un(word))
            break
        else:
            print("The entered word is not in the list. Please try again...\n ")
            continue

    #The below loop prompts user to input data, shows error message if user enters wrong data, calls function 'make_word_groups' and displays the returned string
    while True:   
        vocab_words_list=[['en', 'close', 'joy', 'lighten'],
                 ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete', 'echolalia', 'encoder', 'biography'],
                 ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture'],
                 ['pre', 'serve', 'dispose', 'position', 'requisite', 'digest', 'natal', 'addressed', 'adolescent', 'assumption', 'mature', 'compute'],
                 ['inter', 'twine', 'connected', 'dependent', 'galactic', 'action', 'stellar', 'cellular', 'continental', 'axial', 'operative', 'disciplinary']]

        print("\nSelect a word group(1 2 3 4 5) from the list inorder to add specific prefix to the words\n")
        count=0
        for word_group in vocab_words_list:
            count=count+1
            print(count,word_group)
        try:
            group_option=int(input("Enter a corresponding number - for example: 1 for 1st word group\n"))
            if group_option in range(1,6):
                vocab_words=vocab_words_list[group_option-1]
                print("The final string with group of words by adding prefixes to the words : ",make_word_groups(vocab_words))
                break
            else:
                print("The entered option is not available. Please try again...\n")
                
        except ValueError:
            print("The entered option is invalid. Please input a valid number...\n")
            continue
    
    #The below loop prompts user to input data, shows error message if user enters wrong data, calls function 'remove_suffix_ness' and displays the returned word
    while True:
        wordlist1=['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess']
        print("\nEnter any word from the options below inorder to remove suffix 'ness' \n", wordlist1)
        word=input().lower()
        if word in wordlist1:
            print("Removing suffix 'ness' from the word gives:", remove_suffix_ness(word))
            break
        else:
            print("The entered word is not in the list. Please try again...\n")
            continue

    #The below loop prompts user to input data, shows error message if user enters wrong data, calls function 'adjective_to_verb' and displays the returned verb
    while True:
        sentence_list= ['It got dark as the sun set.',
                      'Look at the bright sky.',
                      'The butter got soft in the sun.',
                      'The morning fog made everything damp with mist.',
                      'He cut the fence pickets short by mistake.']
        index_data = [2, -2, 3, -3, 5]
        print("\nSelect a sentence(1 2 3 4 5) from the below list inorder to change the adjective to verb\n")
        sentence_count=0
        for sent in sentence_list:
            sentence_count=sentence_count+1
            print(sentence_count,sent)
        try:
            option=int(input("Enter a corresponding number - for example 1 for 1st sentence\n"))
            if option in range(1,6):
                sentence=sentence_list[option-1]
                index=index_data[option-1]
                print("Changing adjective to verb: ",adjective_to_verb(sentence,index))
                break
            else:
                print("The entered option is not available. Please try again...\n")
                
        except ValueError:
            print("The entered option is invalid. Please input a valid number...\n")
            continue
        

#Calling the main function
main()