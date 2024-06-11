
# Python program to modify/add Set elements
my_set = {10, 20, 30, 40}
print('Original Set:', my_set)

my_set1 = {10, 25, 30, 35}

#Same in both sets
a=my_set.intersection(my_set1)
print(a)

#Not in Both Sets
b=my_set.difference(my_set1)
print(b)

y = {1, 2, 3}
z = {2, 3, 4}

print(y^(z))

#Subset-If all the elements in a is same as b Thus (FALSE)
r= a<=b

print(r)
