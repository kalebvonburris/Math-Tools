# Calculus I section 5.1.
# Our given function, f(x).
def f(x):
    return 1/(x * (x - 1))

# The number of Reimann rectangles.
R = 6
# The start of the integral.
startCursor = 2
# The end of the integral.
endCursor = 5
# The width of each Reimann rectangle.
width = (endCursor - startCursor) / R
# The point at which each Reimann rectangle is calculated.
origin = 'r'
cursor = 0
if origin == 'm':
    cursor = startCursor + (width / 2)

elif origin == 'l':
    cursor = startCursor

elif origin == 'r':
    cursor = startCursor + width

sum = 0

# Loop for each Reimann rectangle and sum the values.
for i in range(R):
    value = f(cursor)
    # This makes homework way easier. 
    # 8:.5 makes the values round properly and allows padding for larger values.
    print(f'Rectangle {(i + 1):5} has a height of {value:8.5} at x = {cursor:8}')
    sum += value
    cursor += width

# Apply the width of each rectangle. Allows for reversed integrals.
sum *= (endCursor - startCursor) / R
print(f'\nSum:          {sum:.5}')