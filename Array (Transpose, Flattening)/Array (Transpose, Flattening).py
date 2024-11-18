
import numpy  # Import the numpy library for working with arrays

# Read the values of n (number of rows) and m (number of columns)
n, m = map(int, input().split())

# Initialize an empty list to store the rows of the matrix
my_list = []

# Loop to take n rows of input (each row has m integers)
for num in range(n):
    # Read a row of m integers and append it to the list
    val = list(map(int, input().split()[:m]))
    my_list.append(val)

# Convert the list of lists into a numpy array
my_array = numpy.array(my_list)

# Print the transpose of the numpy array (rows become columns and vice versa)
print(numpy.transpose(my_array))

# Print the flattened version of the numpy array (converts it to a 1D array)
print(my_array.flatten())











































