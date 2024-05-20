def lengthOfLastWord(s: str) -> int:
    # trim any leading and trailing spaces
    s = s.strip()
    
    # split the string by spaces
    words = s.split()
    
    # return the length of the last word
    return len(words[-1])

# read input from the user
word = input("Insert your words: ")

# call the function and print the result
print("The words that you have inserted: ", word)
print("The length of the last word: ", lengthOfLastWord(word))

