# Lottery numbers

# In this problem, we've provided you with a set of lottery numbers:

# lottery_numbers = {13, 21, 22, 5, 8}
# You must define a list of two players, each with a name and another set of numbers.

# Players in your list should be dictionaries following this format:
# {
#     'name': 'PLAYER_NAME',
#     'numbers': {1, 2, 3, 4, 5}
# }
# You can come up with each player name and numbers!

# Printing out their luck

# Then for each player, print out a nice string that contains their name and how many numbers they got right (as we've done before,
# you can intersect their numbers with the lottery_numbers  variable provided). You'll then need to calculate the length of the resulting
# set to get how many numbers they got right.

# This string doesn't have to have a particular format, it just must include both the name and how many numbers they got right.

lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name': 'Ali',
        'numbers':  {1, 2, 3, 4, 5}
    },

    {   'name': 'Dhruv',
        'numbers': {13, 21, 4, 5, 8}
    }

]

# Player1 details
player1Name = players[0]["name"]
player1Score = players[0]["numbers"].intersection(lottery_numbers)

# Player2 details
player2Name = players[1]["name"]
player2Score = players[1]["numbers"].intersection(lottery_numbers)

print(f"Player {player1Name} got {len(player1Score)} numbers right")
print(f"Player {player2Name} got {len(player2Score)} numbers right")