"""
Rachel Warner
November 27th, 2020
Program Name: Copy File
Program Purpose:
Write a script that will ask the user for two txt files.
The script will then take the input from one txt file and
output it to the other as a copy.
Inputs:
file name
Outputs:
A copy of the file
"""
# Open a file for txt input
# Ask user for input of the file and reads the text from the file
f = open((input("Please enter a text file to be copied: ")), 'r')
text = f.read()
# Input a file name for the original file to be copied
# Writes the last txt file to a new txt file
c = open((input("Please enter a name for the file to be copied: ")), 'w')
c.write(text)
c.close()