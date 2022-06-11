# Bunny Worker Locations
# ======================
#
# Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a program to match bunny worker IDs to cell locations.
#
# The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas have an unusual layout. They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:
#
# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10
#
# Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.
#
# For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers).
#
# Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large, return your solution as a string representation of the number.

def manhattan(x, y):
    return (x-1)+(y-1)

def maxId(x):
    max = 0
    for i in range(1, x+1):
        max += i
    return max

def solution(x, y):
    m = manhattan(x, y)
    lastId = maxId(m)
    id = lastId + 1 + ((m+1)-y)
    return str(id)

print(1, maxId(1))
print(3, maxId(2))
print(6, maxId(3))
print(10, maxId(4))
print(15, maxId(5))
print(21, maxId(6))
print()

print(0, manhattan(1, 1))
print(1, manhattan(2, 1))
print(2, manhattan(3, 1))
print(1, manhattan(1, 2))
print(3, manhattan(2, 3))
print()

print(1, solution(1, 1))
print(9, solution(3, 2))
print(8, solution(2, 3))
print(96, solution(5, 10))
print()

print(0, solution(100000, 1))
print(0, solution(1, 100000))
