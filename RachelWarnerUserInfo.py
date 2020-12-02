#Ask user for their name
name = input("What is your name?")
#Ask user for their address
address = input("What is your address?")
#Ask user for their telephone
telephone = input("What is your telephone number?")
#Use f-string to format output neatly
print(
  f"User info: \n" +
  f"Name: {name} \n" +
  f"Address: {address} \n" +
  f"Telephone: {telephone} \n"
  )