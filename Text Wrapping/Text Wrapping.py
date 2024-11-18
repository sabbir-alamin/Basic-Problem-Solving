import textwrap  # Import the textwrap module for wrapping text to a specific width

# Define a function to wrap a string into a specified width
def wrap(string, max_width):
    # Use textwrap.fill() to wrap the input string into lines of the given width
    wrapped_text = textwrap.fill(string, width=max_width)
    # Return the wrapped text
    return wrapped_text


# Main entry point of the script
if __name__ == '__main__':
    # Read the input string from the user
    string = input()
    # Read the maximum width for wrapping from the user
    max_width = int(input())
    # Call the wrap function to wrap the input string
    result = wrap(string, max_width)
    # Print the wrapped result
    print(result)

