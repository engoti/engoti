
# Python program to modify/add Set elements
my_set = {10, 20, 30}
print('Original Set:', my_set)

my_set.add(40)
print('Updated Set:', my_set)

my_set.update([50, 60, 70])
print('Updated Set:', my_set)

# using index for updation
# will throw TypeError
my_set[2] = 100
print(my_set)
