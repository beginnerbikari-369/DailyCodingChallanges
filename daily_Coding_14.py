# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.
import random
Interval = 100
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
