# Tuples are immutable, it cannot be changed
friends = ("Ali", "Thalys")
friends = friends + ("Bruno",) # The friends tuple did not change, the new element was just added into the variable
print(friends)