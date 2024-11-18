# Define a function to mutate a string at a specific position with a given character
def mutate_string(string, position, character):
    # Create a copy of the input string
    container = string
    # Convert the string into a list of characters for mutability
    stringer = list(container)
    # Replace the character at the specified position
    stringer[position] = character
    # Join the list back into a string
    container = ''.join(stringer)
    # Return the mutated string
    return container

# Main entry point of the script
if __name__ == '__main__':
    # Read the input string
    s = input()
    # Read the position and character as space-separated inputs
    i, c = input().split()
    # Call the mutate_string function, converting the position to an integer
    s_new = mutate_string(s, int(i), c)
    # Print the mutated string
    print(s_new)
