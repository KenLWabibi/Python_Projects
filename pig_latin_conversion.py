# Ken Wabibi 30jan25 Ch08_lab8-1

'''
                            Programming Lab 8-1  Pig Latin
The purpose of the program is accept an input sentence
and convert each word to a verson of "pig latin" by 
preforming the following task:

1. Removes the first letter at the end of the word.
2. Place the first letter at the end of the word & append the 'ay' to the end.
3. Covert the input and to all upper case.
4. Utilize an outside loop that keeps the program running until stopped by user.
'''

# main function 
def main():
    while True:
        # Prompt for user input
        phrase = input("Type in a phrase to convert to Pig Latin or hit Enter to end the program: ")
       
        # Exit the program if user hits Enter without typing 
        if phrase == "":
            # Displays program has ended
            print("Program Ended.")
            break   # Exit the loop, ending the program
        else:
            # Call the function to convert the phrase to Pig Latin
            pigLatinPhrase = getPigLatinPhrase(phrase)
            # Display results
            print(f"{pigLatinPhrase}")


# function for pig latin conversion
def getPigLatinPhrase(phrase): 
    terms = phrase.split()            # Split the input phrase into individual words
    pigLatinTerms = []                # Stores the converted Pig Latin terms in a list     

    for term in terms:
        term = term.upper()           # Convert the term to uppercase
        pigLatinTerm = term[1:] + term[0] + 'AY'   # Convert the terms to Pig Latin
        pigLatinTerms.append(pigLatinTerm)

    return ' '.join(pigLatinTerms)    # Returns Pig Latin phrase


# function to call main
if __name__ == "__main__":  
    main()




            
        
