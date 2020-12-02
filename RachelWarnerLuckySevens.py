"""
Rachel Warner
November 14th, 2020
Program Name: Lucky Sevens
Program 3.11
Program Purpose: Compute the amount of times it takes
    to lose all of your money while playing Lucky Sevens
    and the maximum amount in the pot at one time.
Input: How money you put in the pot.
Output: Maximum pot amount and turns until $0
"""
#import module from library
from random import randint
print("Welcome to the casino! How about a game of lucky Sevens?")
# Request user for amount in pot
pot = int(input ("How much money would you like to put in the pot? $" ))
# set variables to 0
diOne = 0
diTwo = 0
count = 0
maxVal = 0
# set while loop to run while pot is greater than or equal to 0
while pot >= 0:
    if pot > maxVal:
        maxVal = pot
    diOne = randint(1 , 6)
    diTwo = randint (1 , 6)
    roll = diOne + diTwo
    count += 1
# if roll is 7, add 4, if not, subtract 1
    if roll == 7:
        pot += 4
    else:
        pot -= 1
# output turns until bankrupt and maximum amount in pot
print (f"It took you this many turns to lose all your money: {count}\n" +
       f"However, this is your maximum in your pot at once: ${maxVal}")