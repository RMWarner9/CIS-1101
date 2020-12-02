"""
Program Name: RachelWarnerEmpWeeklyPay.py
Name: Rachel Warner
Date: November 6th, 2020
Program purpose: Compute an employees weekly paycheck
Project 2.10

1 Constants
  Overtime Threshold
  Overtime Factor
2 Inputs
  Wage
  Hours worked
3. Computations:
  Base Pay = Wage * HoursWorked
  Overtime = 1.5 * ((Hoursworked - 40) * wage)
  WeeklyPayCheck = Overtime + Regular Pay
 4. Output 
   paycheck formatted to two digits of precision
"""
# Constants
# This allows us to set the threshold at zero and factor at 2,
# for things like holiday pay: where all time is overtime,
# or make other changes on a per company basis

_overtime_thresh = 40
_overtime_factor = 1.5

# inputs

wage = float(input("Please enter your wage: "))
hoursWorked = float(input("Please enter your hours worked: "))

# computations
# using _overtime_thresh as an internal variable, I compare the two variables hoursWorked and _overtime_thresh
# if the hoursWorked is greater than the _overtime_thresh than we know that the employee worked overtime
if hoursWorked > _overtime_thresh:
    # if overtime hours were worked, basePay is based off the maximum
    # number of base hours worked i.e. overtime threshold
    basePay = float(wage * _overtime_thresh)
    # overtime pay is based off of only the number of hours worked over the overtime threshold
    overtime = float(_overtime_factor * (hoursWorked - _overtime_thresh) * wage)
else:
    # if no overtime was worked, overtime is 0 and basePay is based off of the hours worked
    basePay = float(wage * hoursWorked)
    overtime = 0

# sum the overtime and basePay
weeklyPaycheck = float(overtime + basePay)

# output formatted to currency with two decimals of precision
print("Your weekly paycheck amounts to: $%0.2f" % weeklyPaycheck)
