# Store keys and values, useful for when you know the key and want to return the value back
friend_ages = {
                "Ali": 24,
                "Thalys": 25,
                "Bruno": 34,
            }

friend_ages["Dhruv"] = 24 # Adding a new key/value to a dictionary
friend_ages["John"] = 25

print(friend_ages)

# Example of a tuple with nested dictionary
friends = (
    {"name": "Ali", "age": 24},
    {"name": "Thalys", "age": 25},
    {"name": "Bruno", "age": 34}
)

print(friends[0]["name"])
print(friends[1]["age"])

# Convert list to dictionary
friend = [("Ali", 24), ("Thalys", 25), ("Bruno", 34)]
friend_ages = dict(friend)
print(friend_ages)


# Example of list and set
players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]
print(players[0]['numbers'])
print(players[0]['numbers'][0])