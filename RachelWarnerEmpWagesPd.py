"""
Rachel Warner
November 27th, 2020
Program Name: EmpWagesPd
Program Purpose:
Create a program that takes input from a text file with the lines having 3 variables
<last name>, <hours worked> <wage>
takes the inputted file from the user, and prints to the terminal in
a tabular format with appropriate headers. Displays their total earnings for the pay period
Input: Txt file:
Output: A Tabular output into the terminal of the employee name, hours worked, their wage and their total amount
payed for the pay period.
"""
# Asks the user for Employee Pay txt file
file_name = input("Please Enter a file name for Employee Pay: ")

# Gathers the data from the txt file and separates it
def read_list_file(path: str):
    with open(path) as f:
        lines = f.read().split()
        data = []
        for line in lines:
            data.append(line.split(" "))
        return data


# Set headers for table
data = read_list_file(file_name)
# Sets width for table
COLUMN_A_WIDTH = 25
COLUMN_B_WIDTH = 12
COLUMN_C_WIDTH = 6
COLUMN_D_WIDTH = 7
# Prints the headers
print(
    f"|{'Last Name'.ljust(COLUMN_A_WIDTH)}|{'Hours Worked'.ljust(COLUMN_B_WIDTH)}|{'Rate'.ljust(COLUMN_C_WIDTH)}|{'Pay'.ljust(COLUMN_D_WIDTH)}|")
# For each row in the table, assign the data by the row and assigns it with the output
for row in data:
    hours = float(row[1])
    rate = float(row[2])
    formatted_rate = f"{rate:.2f}"
    pay = f"{(hours * rate):.2f}"
    print(
        f"|{row[0].ljust(COLUMN_A_WIDTH)}|{str(hours).ljust(COLUMN_B_WIDTH)}|{formatted_rate.ljust(COLUMN_C_WIDTH)}|{pay.ljust(COLUMN_D_WIDTH)}|")
