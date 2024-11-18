# Read the size of the first list
m = int(input())
# Read 'm' space-separated integers, convert them to a list, and slice it to ensure the size is 'm'
lister = list(map(int, input().split()))[:m]
# Convert the list to a set to store unique elements
set1 = set(lister)

# Read the size of the second list
n = int(input())
# Read 'n' space-separated integers, convert them to a list, and slice it to ensure the size is 'n'
lister1 = list(map(int, input().split()))[:n]
# Convert the list to a set to store unique elements
set2 = set(lister1)

# Find the elements present in set1 but not in set2
k = set1.difference(set2)
# Find the elements present in set2 but not in set1
l = set2.difference(set1)

# Create an empty set (unnecessary here, as it's overwritten in the next step)
reform = set()

# Find the symmetric difference of the two sets (elements unique to each set)
z = k.symmetric_difference(l)

# Convert the resulting set to a sorted list
new_list = list(z)
new_list.sort()

# Print each element of the sorted list on a new line
for num in new_list:
    print(num)









