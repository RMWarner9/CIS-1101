"""
Program: RachelWarnerTaxFormRound.py
Author: Rachel Warner
Date: November 6th, 2020
Program Purpose: Compute a person's income tax
Project 2.1
1. Significant Constants:
  tax rate
  standard deduction
  deduction per dependent
2. The inputs are
  gross income
  number of dependents
3. Computations
  taxable income = gross income - the standard deduction - a deduction per dependent 
  income tax = fixed percentage of the taxable income
4. The outputs are
  the income tax formated to two digits of precision
"""
# constants
_TAX_RATE = 0.20
_STANDARD_DEDUCTION = 10000.00
_DEPENDENT_DEDUCTION = 3000.00

# inputs
grossIncome = float(input("Please enter your gross income: "))
numDependents = int(input("Please enter the number of dependents: "))

# Computing the income tax
taxableIncome = grossIncome - _STANDARD_DEDUCTION - (_DEPENDENT_DEDUCTION * numDependents)
incomeTax = float(taxableIncome * _TAX_RATE)

# output
print("The income tax is: $%0.2f" % incomeTax )

