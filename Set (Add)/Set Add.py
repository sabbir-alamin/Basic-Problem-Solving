
# Initialize an empty set to store unique values

collection = set()

# Read the number of elements to be added to the collection
N = int(input())  # Input: Number of values to be entered

# Loop through the range of N to collect input values
for _ in range(0, N):
    val = input()  # Input: A value to be added to the collection
    collection.add(val)  # Add the value to the set (ensures uniqueness)

# Initialize another empty set to process unique values further
plus = set()

# Iterate through each unique value in the 'collection' set
for amount in collection:
    # If the value is not already in 'plus', add it to 'plus'
    if amount not in plus:
        plus.add(amount)  # Add value to 'plus'

# Print the total count of unique values in 'plus'
print(len(plus))

