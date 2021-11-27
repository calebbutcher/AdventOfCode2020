# Part 1
with open("input.txt", "r") as input:
    valid_passwords = 0

    for line in input:
        line = line.replace(": ", " ").replace("-", " ")
        line = line.split(" ")

        min_times = int(line[0])
        max_times = int(line[1])
        target = line[2]
        password = line[3]
        cnt = password.count(target)

        if min_times <= cnt <= max_times:
            valid_passwords += 1
print("Part 1")
print("Number of Valid Passwords:", valid_passwords)

# Part 2
# Slightly different rules this time around!

with open("input.txt", "r") as input:
    valid_passwords = 0

    for line in input:
        line = line.replace(": ", " ").replace("-", " ")
        line = line.split(" ")

        first_pos = int(line[0])
        second_pos = int(line[1])
        target = line[2]
        password = line[3]

        first_char = password[(first_pos -1)]
        second_char = password[(second_pos -1)]

        if first_char == target or second_char == target:
            if first_char != second_char:
                valid_passwords += 1
print("Part 2")
print("Number of Valid Passwords:", valid_passwords)   

