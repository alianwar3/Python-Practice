# List - a single variable containing similiar values (data should be related)
friends = [['Ali', 24], ['Thalys', 25], ['Bruno', 34]]
print(friends[1][1]) # Access a list element passing the index value
print(len(friends)) # Get length of list

# If the list is long, its good to split the list into multiple lines
friends2 = [
    ['Ali', 24],
    ['Thalys', 25],
    ['Bruno', 34],
    ['Dhruv', 24]
]

# Use 'append' to add to a list
friends.append(['Dhruv', 24])

# Use 'remove' to remove value from the list
friends.remove(["Thalys", 25])
print(friends)

# Joining a list
friend = ["Ali", "Shah", "Fred"]
comma_seperated = ", ".join(friend)
print(f"My friends are {comma_seperated}")