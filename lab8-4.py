"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
_____________________________________________________________________________________

Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num

_______________________________________________________________________________________

Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.



"""
def count_a(word):
    # Initialize a counter for 'a's
    a_count = 0
    
    # Iterate through each character in the word
    for char in word:
        # Check if the character is 'a' or 'A' and increment the counter
        if char == 'a' or char == 'A':
            a_count += 1
            
    # Return the final count of 'a's
    return a_count
# Author: Nazeer thompson
