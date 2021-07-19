# Exercise_1
# first variant of the brackets
x = (2 + 2 * 2 - 2) / 2
print(x)
# second variant of the brackets
x = 2 + 2 * (2 - 2) / 2
print(x)

# Exercise_2
# for the long scripts deposit can be defined through the input
deposit = 2130
years = 1
# added additional input fot the variable, just think that it is easier to change it then to look for it in the script
n = int(input("Please input the number of years for your deposit"))
while years <= n:
    deposit = deposit + (deposit * 0.1 + 120)
    years += 1
print(deposit)



# Exercise_3
