# Whats your choice
number_of_days = int(input("Enter number of days: "))
# Years
years = number_of_days // 365
# Months
months = (number_of_days - years *365) // 30
# Days
days = (number_of_days - years * 365 - months*30)
# These are the outputs
print("Years = ", years)
print("Months = ", months)
print("Days = ", days)