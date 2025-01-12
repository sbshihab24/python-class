#Logical Operators(and,or,not)
x = 10
y = 5
print(x > 5 and y < 10)  # True, because both conditions are True
print(x > 15 and y < 10) # False, because the first condition is False
print(x==10 and y==5)    # True, because both conditions are True


print(x > 5 or y > 10)  # True, because the first condition is True
print(x < 5 or y > 10)  # False, because both conditions are False
print(x==10 or y==x)     #True, because the first condition is True

print(not (x > 5))  # False, because x > 5 is True
print(not (x < y))  # True, because x < 5 is False

#Combining Logical Operators
x = 10
y = 5
z = 15

# Combining 'and' and 'or'
print((x > y) and (y < z))  # True, because both conditions are True
print((x > y) or (y > z))   # True, because at least one condition is True

# Using 'not' with 'and'
print(not (x > y and y < z)) # False, because the original condition is True

