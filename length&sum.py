grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)


grades  = [80, 75, 90, 100] # Good option b/c we can add new grades, remove grades, and have duplicates
grades2 = (80, 75, 90, 100) # Bad option b/c we cannot change the tuple, hence we cannot update grades
grades3 = {80, 75, 90, 100} # Bad option b/c we cannot have duplicate grades in a set