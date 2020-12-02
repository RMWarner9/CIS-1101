"""
Name: Rachel Warner
Date: December 1st, 2020
Program Name: Unique
Program Purpose:
   Create a program that takes an input of a file and then
   returns the words in the file in alphabetical order
Input: Prompts the user for a file for the input
Output: Outputs the words in the file to be sorted alphabetically
"""
# Prompts the user to input a file name
fileName = input("Enter a file name for the words to be sorted alphabetically: ")


def read_lines(path: str):
   # The function takes a file path and seperates the words and lines to become seperate elements
    with open(path) as f:
        words = []
        lines = f.read().split()
        for line in lines:
            words.append(line)
        return words

# Set a variable equal to the completed list to prevent the None return.
file = read_lines(fileName)
# Sorts the list
file.sort()
# Outputs the list
print(file)
