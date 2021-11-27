from math import prod

def getNumbers(numbers, nums_used, goal):
    length = len(numbers)

    if nums_used < 1 or nums_used > length:
        return

    last_indicie_index = nums_used -1
    indices = [i for i in range(nums_used)]

    checks =0
    while True:
        checks += 1
        # Checking if selected numbers equal our goal
        numbs = [numbers[indice] for indice in indices]
        if sum(numbs) == goal:
            return numbs

        indices[last_indicie_index] += 1

        # Going to next index if needed
        for i in range(nums_used-1, 0, -1):
            min_indice = max(indices[:i]) + 1
            max_indice = length - nums_used + i
            if indices[i] > max_indice:
                indices[i-1] += 1
                indices[i] = min_indice
        
        # Checking if we have hit end of list
        if indices[0] > length - nums_used:
            return

goal = 2020

with open("input.txt", "r") as file:
    numbers = [int(number) for number in file]

# Part 1
print ("Part 1")
result = getNumbers(numbers, 2, goal)
print("Entries:", result)
if result:
    print("Entries Product:", prod(result))

print()

# Part 2
print("Part 2")
result = getNumbers(numbers, 3, goal)
print("Entries:", result)
if result:
    print("Entries Product:", prod(result))