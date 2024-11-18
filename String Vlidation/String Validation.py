if __name__ == '__main__':

    value = input()
    global letters  # making letters global scoped

# checks if the value has any alphanumeric value

    for letters in value:
        if letters.isalnum():
            print("True")
            break

    if not letters.isalnum():
        print("False")

# checks if the value has any alphabetic value

    for letters in value:
        if letters.isalpha():
            print("True")
            break

    if not letters.isalpha():
        print("False")

# checks if the value has any numeric value

    for letters in value:
        if letters.isdigit():
            print("True")
            break

    if not letters.isdigit():
        print("False")

# checks if the value is lower-cased value

    for letters in value:
        if letters.islower():
            print("True")
            break

    if not letters.islower():
        print("False")

# checks if the value is upper-cased value

    for letters in value:
        if letters.isupper():
            print("True")
            break

    if not letters.isupper():
        print("False")





