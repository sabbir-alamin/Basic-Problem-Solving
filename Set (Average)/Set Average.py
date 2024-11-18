# Define a function to calculate the average of unique numbers in an array
def average(array):
    # Convert the array into a set to keep only unique elements
    num_set = set(array)
    # Calculate the sum of all unique elements
    value = sum(num_set)
    # Find the number of unique elements
    length = len(num_set)
    # Compute the average by dividing the sum by the count
    avg = value / length
    # Format the average to 3 decimal places
    former = format(avg, '.3f')
    # Return the formatted average
    return former

# Main entry point of the script
if __name__ == '__main__':
    # Read an integer 'n' (number of elements in the array)
    n = int(input())  
    # Read 'n' space-separated integers and convert them into a list
    arr = list(map(int, input().split()))  
    # Call the average function and store the result
    result = average(arr)
    # Print the result
    print(result)