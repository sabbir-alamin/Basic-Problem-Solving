if __name__ == '__main__':
    N = int(input())  # Read the number of commands

    command = []

    for all_command in range(N):  # Loop to read N commands
        value = input().split()  # Split input into a list
        command.append(value)  # Add the parsed command to the command list

    # Convert numerical values in the commands from strings to integers
    for comm in range(len(command)):
        if len(command[comm]) == 3:  # If the command has three parts (e.g., 'insert x y')
            var = int(command[comm][1])  # Convert the second part to an integer
            var2 = int(command[comm][2])  # Convert the third part to an integer
            command[comm][1] = var
            command[comm][2] = var2

        if len(command[comm]) == 2:  # If the command has two parts (e.g., 'append x')
            var3 = int(command[comm][1])  # Convert the second part to an integer
            command[comm][1] = var3

    empty = []

    # Iterate through the list of commands and execute the corresponding operations
    for methods in command:
        if len(methods) == 3:  # Commands with three parts, e.g., 'insert x y'
            if "insert" in methods:  # Insert value at a specific position
                empty.insert(methods[1], methods[2])

        if len(methods) == 2:  # Commands with two parts, e.g., 'append x', 'remove x'
            if "remove" in methods:  # Remove the first occurrence of a value
                empty.remove(methods[1])

            elif "append" in methods:  # Add a value to the end of the list
                empty.append(methods[1])

        if len(methods) < 2:  # Commands with no additional arguments, e.g., 'print', 'pop', 'sort', 'reverse'
            if "sort" in methods:  # Sort the list in ascending order
                empty.sort()

            elif "pop" in methods:  # Remove the last element of the list
                empty.pop()

            elif "reverse" in methods:  # Reverse the order of the list
                empty.reverse()

            elif "print" in methods:  # Print the current state of the list
                print(empty)