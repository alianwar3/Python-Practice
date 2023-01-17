age = 25

# The 'and' keyword specifies that both conditions below are true
result = age > 18 and age < 65 # Both results will produce true

# The 'or' keyword specifies if either option is true
result2 = age < 18 or age < 65


# 0, "", [] will be evaluated as false
# Valid values will be evaluated as true
default_age = 30
age = 0

user_age = age or default_age

default_greeting = "there"
name = input("Enter your name: (optional)")

user_name = name or default_greeting
print(f"Hello, {user_name}!")    # this will print there if name is falsy, however if the name is truthy it will return name contents