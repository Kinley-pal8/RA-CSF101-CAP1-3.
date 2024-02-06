################################
# Kinley Palden
# Section A 
# 02230287
################################
# REFERENCES
# Links that you referred while solving the problem
# https://nedbatchelder.com/blog/201310/range_overlap_in_two_compares.html
# https://bobbyhadz.com/blog/find-range-overlap-in-python-or-check-if-ranges-overlap
# https://www.tutorialspoint.com/check-if-any-interval-completely-overlaps-the-other-in-python
# https://www.w3schools.com
################################
# SOLUTION
# Your Solution Score:
# Task 1: There were 20000 people assigned and there are 6515 overlapping space assignments.
# Task 2: There were 6515 assignments that overlap completely.
################################

# Read the input.txt file
# Read lines from a file.
def read_input(filename="CAP2/input_7_cap2.txt"):
#Args:
#filename (str): The name of the file to read from. Defaults to "CAP2/input_7_cap2.txt".
#Returns:
#list: A list containing each line of the file as a string.
#If the file is not found, an empty list is returned, and a message is printed to indicate the error.
    try:
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()  
        return lines
    except FileNotFoundError:
        # Print error message if file is not found
        print(f"File {filename} not found.") 
        # Return an empty list if file is not found
    return []  

# solution
def task_1(lines):   
# Assuming each line represents one person with two ranges
    total_people = len(lines) * 2 
# Sum up the overlaps for each line
    total_overlaps = sum(count_overlaps(concat_line(line)) for line in lines)

#Concatenate a line into a range list.
def concat_line(line):
    # Split the line by ', ' to separate the ranges
    ranges = line.strip().split(', ')
    # Convert each range into a list of integers representing the start and end points
    return [[int(num) for num in range_.split('-')] for range_ in ranges]

#Count the number of overlapping spaces.
def count_overlaps(spaces):
    total_overlaps = 0
    n = len(spaces)
    # Iterate over each pair of ranges
    for x in range(n):
        for y in range(x + 1, n):
            # Check for overlap by comparing start and end points
            if max(spaces[x][0], spaces[y][0]) <= min(spaces[x][1], spaces[y][1]):
                total_overlaps += 1
    return total_overlaps


def task_2(lines):
    # Since we're counting complete overlaps, the logic is the same as task 1
    total_complete_overlaps = sum(count_overlaps(concat_line(line)) for line in lines)
    

if __name__ == "__main__":
# Read lines from the input file
    lines = read_input()
    
# concatenated lines and count overlaps simultaneously
    # Assuming each line represents one person with two ranges
    total_people = len(lines) * 2  
    total_overlaps = 0
    total_complete_overlaps = 0
    
# Iterate over each line
    for line in lines:
        # Concatenate each line into ranges
        ranges = concat_line(line)
        # Count overlaps for each range
        overlaps = count_overlaps(ranges)
        total_overlaps += overlaps
        # Count complete overlaps
        # If all pairs overlap
        if overlaps == len(ranges) * (len(ranges) - 1) // 2:  
            total_complete_overlaps += 1
    
# Print results
    print(f"There were {total_people} people assigned and there are {total_overlaps} overlapping space assignments.")
    print(f"There were {total_complete_overlaps} assignments that overlap completely.")



# Other parts of code here to run your functions and printing of the required solution.

# Note: You may add parameters/arguments, return values to the functions above.