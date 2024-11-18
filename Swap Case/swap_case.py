# Define a function to swap the case of characters in a string
def swap_case(s):
    # Initialize an empty string to store the modified result
    add = ''
    adder = ''  # This variable seems unused and redundant

    # Iterate through each character in the string
    for j in s:
        # Check if the character is a space and append 'adder' (currently unused)
        if j.isspace():
            add += adder

        # If the character is lowercase, convert it to uppercase
        if j.islower():
            add += j.upper()

        # If the character is uppercase, convert it to lowercase
        if j.isupper():
            add += j.lower()

        # If the character is neither uppercase nor lowercase (e.g., symbols, digits), append it as is
        if not j.isupper() and not j.islower():
            add += j

    # Return the resulting string with swapped cases
    return f"{add}"


# Main entry point of the script
if __name__ == '__main__':
    # Read the input string from the user
    s = input()
    # Call the swap_case function and store the result
    result = swap_case(s)
    # Print the modified string
    print(result)


