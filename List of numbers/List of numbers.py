if __name__ == '__main__':

    x = int(input())  # Input for the range of x values
    y = int(input())  # Input for the range of y values
    z = int(input())  # Input for the range of z values
    n = int(input())  # Condition for filtering the combinations

    x_list = [value for value in range(x)]  # List of integers from 0 to x-1
    y_list = [val for val in range(y)]  # List of integers from 0 to y-1
    z_list = [value for value in range(z)]  # List of integers from 0 to z-1

    # Initialize an empty list to store combinations
    num_list = []

    # Generate all possible combinations of x, y, z
    for xx in range(len(x_list) + 1):  # Iterate through the range of x_list + 1
        for yy in range(len(y_list) + 1):  # Iterate through the range of y_list + 1
            for zz in range(len(z_list) + 1):  # Iterate through the range of z_list + 1
                # Append the combination [xx, yy, zz] to num_list
                num_list.append([xx, yy, zz])

    # Filter combinations where the sum is not equal to n
    new_list = [new_val for new_val in num_list if sum(new_val) > n or sum(new_val) < n]

    # Print the filtered list of combinations
    print(new_list)