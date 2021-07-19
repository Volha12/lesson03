deposit = 2130
years = 1
bonus = 120
# decided to add fot the variable, just think that it is easier to change it then to look for it in the script
n = int(input("Please input the number of years for your deposit "))
while years <= n:
    deposit = deposit + (deposit * 0.1 + bonus)
    years += 1
print(deposit)