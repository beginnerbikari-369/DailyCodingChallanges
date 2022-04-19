import random
Interval = 10000
circle_points = 0
square_points = 0
PI = 0
for i in range(Interval ** 2):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x ** 2 + y ** 2) <= 1:
        circle_points += 1
    square_points += 1
    PI = 4 * (circle_points / square_points)
print("pi value = ", PI)
