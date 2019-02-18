# Create a firtree with asterisks

# Ask for the user input
initialcounter = 3
# int(input("How many branches?"))

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

import queue
list = [1,2,3,4]
q = queue.PriorityQueue()

q.put((10,"Halo"))
q.put((15,"Mars"))
q.put((5,"Phobos"))
print(q.get())

d = {}
text = "A A A A A A B B B B B B B B B B B D D D D D D D F F F F"
for word in text.split(" "):
    if word in d:
        d[word] = d[word] +1
    else:
        d[word] = 1

print(d)
