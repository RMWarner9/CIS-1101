"""
Rachel Warner
November 13th, 2020
Program 3.9
Program Name: Sum Avg
Program Purpose: This program will take inputs from the user until the user just presses enter. Once the inputs are finished,
   The program will calulate the sum and average of the input values.
Inputs are from the user
Outputs are the sum and average
"""
#setting the variables to 0

theSum = 0.0
count = 0
print("Let me calculate the sum and average for you!")
#the loop will continue until the statement becomes false with the if statement
while True:
    count += 1
    #user inputs numbers
    data = input ("Enter a number or press enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
#Average is calulated by dividing by count - 1 to prevent a 1 off error
#due to "" counting as a loop/count
Average = (theSum / (count - 1))
#outout sum and average of data values
print(f"The sum is: {theSum} \n" +
      f"The average is: {Average}"
      )