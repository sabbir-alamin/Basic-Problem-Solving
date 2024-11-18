# Taking two input numbers: x (number of subjects) and y (number of students)
x, y = map(int, (input().split()))

all_num = []  # Initialize an empty list to store the scores of all students

# Loop to store the number of different student scores for different subjects
for var in range(0, y):
    # Read the student's scores for each subject as a list of floats
    number = list(map(float, (input().split())))[:x]
    all_num.append(number)  # Append the list of scores for the student

# Using zip() to transpose the nested list and convert it into a list of tuples
# Each tuple contains the scores for a specific subject across all students
value = list(zip(*all_num))

# Loop through each subject (i.e., each tuple in the transposed list)
for val in range(len(value)):
    # Convert the tuple of scores for a subject into a list
    var = list(value[val])
    # Calculate the total number of scores for this subject (length of the list)
    length = len(var)
    # Calculate the sum of the scores
    total_num = sum(var)
    # Calculate the average score for this subject
    avg = total_num / length
    # Print the average score for the current subject
    print(avg)





