# Function to calculate rubber duck type based on time
def get_duck_type(time):
    if 0 <= time <= 60:
        return "Darth Vader Ducky"
    elif 61 <= time <= 120:
        return "Thor Ducky"
    elif 121 <= time <= 180:
        return "Big Blue Rubber Ducky"
    elif 181 <= time <= 240:
        return "Small Yellow Rubber Ducky"


# Read input sequences
programmer_times = list(map(int, input().split()))
task_counts = list(map(int, input().split()))

# Initialize dictionary to store duck counts
duck_counts = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmer_times and task_counts:
    # Calculate the time needed for the current task
    time_needed = programmer_times[0] * task_counts[-1]

    # Check if the time falls within the specified range
    if 0 <= time_needed <= 240:
        duck_type = get_duck_type(time_needed)
        duck_counts[duck_type] += 1
        programmer_times.pop(0)
        task_counts.pop()
    else:
        # Reduce the number of tasks by 2 and move the programmer time to the end
        task_counts[-1] -= 2
        programmer_times.append(programmer_times.pop(0))

# Output the results
print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {duck_counts['Darth Vader Ducky']}")
print(f"Thor Ducky: {duck_counts['Thor Ducky']}")
print(f"Big Blue Rubber Ducky: {duck_counts['Big Blue Rubber Ducky']}")
print(f"Small Yellow Rubber Ducky: {duck_counts['Small Yellow Rubber Ducky']}")