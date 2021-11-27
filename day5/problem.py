input = open('input.txt').read().strip('\n')
input = input.splitlines()


# Part 1
seats = [int(x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for x in input]
seats.sort()
print("Part 1")
print("The highest Seat ID is:",seats[-1])


# Part 2
for x in range(len(seats)):
    if seats[x+1] - seats[x] != 1:
        print("Part 2")
        print("Your Seat ID is:",seats[x] + 1)
        break
