if __name__ == '__main__':
    # Main entry point of the script

    # Read an integer input, which represents the number of elements in the tuple
    n = int(input(""))

    # Read a space-separated list of integers, convert them to a tuple, and limit the tuple to 'n' elements
    integer_tuple = tuple(map(int, input().split()))[:n]

    # Compute the hash of the tuple and print it
    print(hash(integer_tuple))
