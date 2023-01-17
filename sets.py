# Sets don't have order, or they do not contain duplicates
# art_friends = {"Rolf", "Anne"}
# science_friends = {"Jen", "Charlie"}

# art_friends.add("Jen")
# print(art_friends)
# art_friends.remove("Jen")
# print(art_friends)

# Advanced set operations
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends) # difference gives what elements in art, but not in science
science_but_not_art = science_friends.difference(art_friends) # difference gives what elements in science, but not in art

not_in_both = art_friends.symmetric_difference(science_friends) # what elements are not both sets
art_and_science = art_friends.intersection(science_friends) # what is in both sets
all_friends = art_friends.union(science_friends) # combine both sets together