################################
# Kinley Palden
# Section A
# 02230287
################################
# REFERENCES
# Links that you referred while solving the problem 
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.geeksforgeeks.org/python-map-function/
#https://realpython.com/read-write-files-python/
#
################################
# SOLUTION
# Your Solution Score: 
# 50169
################################

# solution
def calculate_score(opponent_choice, desired_outcome):
    # Define the score for each choice
    choices = {'A': 1, 'B': 2, 'C': 3}

    # Define the mappings for winning, losing, and drawing outcomes
    outcomes = {
        'X': {'A': 'C', 'B': 'A', 'C': 'B'},  # Winning outcomes
        'Y': {'A': 'A', 'B': 'B', 'C': 'C'},  # Drawing outcomes
        'Z': {'A': 'B', 'B': 'C', 'C': 'A'}   # Losing outcomes
    }

    # Decide what to play based on the desired outcome
    your_choice = outcomes[desired_outcome][opponent_choice]

    # Calculate the score for the round
    score = choices[your_choice]

    # Add the outcome to the score
    if desired_outcome == 'Y':
        score += 3  # Drawing outcome
    elif desired_outcome == 'Z':
        score += 6  # Losing outcome

    return score

# Read the input.txt file
def read_input():
    # Open the input file
    with open(r"/home/blackjesus/Desktop/CSF/RA CAP/CAP1/input_7_cap1.txt", 'r') as file:
        total_score = 0
        # Iterate through each line in the file
        for line in file:
            # Extract opponent's choice and desired outcome from the line
            opponent_choice, desired_outcome = line.strip().split()
            # Calculate the score for the round
            score = calculate_score(opponent_choice, desired_outcome)
            # Accumulate the total score
            total_score += score
        # Print the total score
        print(f'The total score is: {total_score}')

# Entry point of the script
if __name__ == "__main__":
    read_input()  # Call the main function when the script is executed

# Other parts of code here to run your functions and printing of the input.

# Note: You may add parameters/arguments, return values to the functions above.