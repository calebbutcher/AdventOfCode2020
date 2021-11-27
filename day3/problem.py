input = open('input.txt').read().strip('\n')
input = input.splitlines()

#print(input)

#Part 1
def collisions(map, rise, run):
    hit = 0
    x = 0
    y = 0
    while True:
        y = y + rise
        if y >= len(map):
            break
        x = (x + run) % len(map[y])
        if map[y][x] == '#':
            hit = hit + 1
    return hit

print("Part 1")
print("Number of collisions:", collisions(input, 1, 3))


# Part 2
prod = 1
for slopes in [[1,1],[1,3],[1,5],[1,7],[2,1]]:
    prod = prod * collisions(input,slopes[0],slopes[1])
print("Part 2")
print("Product of Collisions:", prod)
