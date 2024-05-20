# Halstead length: length of last word
# Question

Given a string s consisting of words and spaces, return the length of the last word in the string.
 *a word is a maximal substring consisting of non-space characters only.

# Code explanation

def lengthOfLastWord(s: str) -> int: 
---------------------
defines a function named lengthOfLastWord that takes a single argument s of type str (string) and returns an integer (int). 
The type hints (s: str and -> int) help indicate what type of input the function expects and what type of output it will produce.

words = s.strip() 
---------------
splits the trimmed string s into a list of words using the split() method. The split() method by default splits
the string by any whitespace (spaces, tabs, newlines) and returns a list of words.

return len(words[-1])
---------------
returns the length of the last word in the list words. The [-1] index is used to access the last element of the list. 
The len() function then calculates the length of that word.

Reading Input from the User
---------------
word = input("Insert your words: ")

Calling the function and printing the result
---------------
print("The words that you have inserted: ", word)
print("The length of the last word: ", lengthOfLastWord(word))


# Full Execution Summary:
If the user inputs "Hello my name is Misheel", the program will execute the following steps:

- Trim any leading and trailing spaces from the input (none in this case).
- Split the string into a list of words: ["Hello", "my", "name", "is", "Misheel"].
- Return the length of the last word, which is "Misheel" with length 7.


# Halstead metrics
a metric used in software engineering to measure the complexity of a program
- Operators: Symbols or keywords that perform operations (e.g., +, -, *, /, if, while, return)
- Operands: Variables, constants, or values on which the operators act (e.g., x, y, 5, "hello")

The Halstead length (N)
---------------
the total number of operator and operand occurrences in the program. Calculated as: 𝑁= 𝑁1+𝑁2
where:
- N1 is the total count of operators.
- N2 is the total count of operands.

The Halstead volume (V)
---------------
measure the complexity and size of a software program. It quantifies the amount of information or cognitive load required to understand the program.

Halstead Volume (V) is calculated using the following formula: 𝑉= 𝑁×log2(𝑛)
Where:
- N is the Halstead Length, which represents the total number of operator and operand occurrences in the program.
- n is the Halstead Vocabulary, which represents the total number of unique operator and operand types used in the program.
- log2 denotes the base-2 logarithm.


# Calculation

Distinct Operators 14: def, (, ), :, #, =, ., strip, split, return, len, input, print, ,
Distinct Operands 7: lengthOfLastWord, s, str, int, words, word, words[-1]

Total Operators (N1): 24 (including each occurrence of def, (, ), :, #, =, ., strip, split, return, len, input, print, ,)
Total Operands (N2): 14 (including each occurrence of lengthOfLastWord, s, str, int, words, word, words[-1])

Halstead Vocabulary:   n=n1+n2   ----->  n=14+7=21
Halstead Length:       N=N1+N2  ----->  N=24+14=38
Halstead Volume:
V= N×log2​(n)   𝑉= 38×log⁡2(21)   
log⁡2(21)≈ 4.392log2
​V≈ 38 × 4.392= 166.896









