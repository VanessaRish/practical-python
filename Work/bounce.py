# bounce.py
#
# Exercise 1.5

height = 100
step = 1

while step <= 10:
    height *= 3 / 5
    print(step, round(height, 4))
    step += 1

