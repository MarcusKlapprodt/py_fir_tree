# Create a firtree with asterisks

# Ask for the user input
initialcounter = int(input("How many branches?"))

# Set up the variables
branches = initialcounter
star = "*"
sterncounter = 1
treetrunk = int(initialcounter/3)

# Create the "branches" with a for-loop
for rows in range(branches):
    print(branches * " " + sterncounter * star)
    branches -= 1
    sterncounter += 2

# Create the trunk with another for-loop

for trunk in range(treetrunk):
    print(initialcounter * " " + star)

# Print a season's greetings message
print(" ")
print(" ")
print("season's greetings!")