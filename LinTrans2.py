import matplotlib.pyplot as plt

# Standard House
# Define the x and y coordinates of the House body
x_body = [0, 1, 1, 0]
y_body = [0, 0, 0.5, 0.5]

# Define the x and y coordinates of the House roof
x_roof = [0.2, 0.8, 1, 0]
y_roof = [0.7, 0.7, 0.5, 0.5]

# Define the x and y coordinates of the House Doors
x_wheel_left = [0.2, 0.3, 0.3, 0.2]
y_wheel_left = [0, 0, 0.2, 0.2]
x_wheel_right = [0.7, 0.8, 0.8, 0.7]
y_wheel_right = [0, 0, 0.2, 0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the House body using the fill() function
ax.fill(x_body, y_body, color='red')

# Plot the House roof using the fill() function
ax.fill(x_roof, y_roof, color='gray')

# Plot the House House using the fill() function
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Add some labels and formatting to the plot
ax.set_title('House Sketch - Normal')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

# Show the plot
plt.show()


# REFLECTION THROUGH THE HORIZONTAL AXIS
# Define the x and y coordinates of the House body
x_body = [-0.0, -1.0, -1.0, -0.0]
y_body = [-0.0, -0.5, -0.5, -0.0]

# Define the x and y coordinates of the House roof
x_roof = [-0.2, -0.8, -1.0, -0.0]
y_roof = [-0.5, -0.5, -0.0, -0.0]

# Define the x and y coordinates of the House House
x_wheel_left = [-0.2, -0.3, -0.3, -0.2]
y_wheel_left = [-0.0, -0.0, -0.2, -0.2]
x_wheel_right = [-0.7, -0.8, -0.8, -0.7]
y_wheel_right = [-0.0, -0.0, -0.2, -0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the original House using the fill() function
ax.fill(x_body, y_body, color='red')
ax.fill(x_roof, y_roof, color='gray')
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Reflect the House over the horizontal axis
y_body_reflected = [-y for y in y_body]
y_roof_reflected = [-y for y in y_roof]
y_wheel_left_reflected = [-y for y in y_wheel_left]
y_wheel_right_reflected = [-y for y in y_wheel_right]

# Plot the reflected House using the fill() function
ax.fill(x_body, y_body_reflected, color='red', alpha=0.5)
ax.fill(x_roof, y_roof_reflected, color='gray', alpha=0.5)
ax.fill(x_wheel_left, y_wheel_left_reflected, color='black', alpha=0.5)
ax.fill(x_wheel_right, y_wheel_right_reflected, color='black', alpha=0.5)

# Add some labels and formatting to the plot
ax.set_title('House Sketch (Reflection - Horizontal)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([-2.0, 2.0])
ax.set_ylim([-2.0, 2.0])

# Show the plot
plt.show()


# Define the x and y coordinates of the House body
x_body = [-0.0, -1.0, -1.0, -0.0]
y_body = [-0.0, -0.5, -0.5, -0.0]

# Define the x and y coordinates of the House roof
x_roof = [-0.2, -0.8, -1.0, -0.0]
y_roof = [-0.5, -0.5, -0.0, -0.0]

# Define the x and y coordinates of the House House
x_wheel_left = [-0.2, -0.3, -0.3, -0.2]
y_wheel_left = [-0.0, -0.0, -0.2, -0.2]
x_wheel_right = [-0.7, -0.8, -0.8, -0.7]
y_wheel_right = [-0.0, -0.0, -0.2, -0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the original House using the fill() function
ax.fill(x_body, y_body, color='red')
ax.fill(x_roof, y_roof, color='gray')
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Invert the signs of both the x and y coordinates to reflect the House through the origin
x_body_reflected = [-coord for coord in x_body]
y_body_reflected = [-coord for coord in y_body]
x_roof_reflected = [-coord for coord in x_roof]
y_roof_reflected = [-coord for coord in y_roof]
x_wheel_left_reflected = [-coord for coord in x_wheel_left]
y_wheel_left_reflected = [-coord for coord in y_wheel_left]
x_wheel_right_reflected = [-coord for coord in x_wheel_right]
y_wheel_right_reflected = [-coord for coord in y_wheel_right]

# Plot the reflected House using the fill() function
ax.fill(x_body_reflected, y_body_reflected, color='red', alpha=0.5)
ax.fill(x_roof_reflected, y_roof_reflected, color='gray', alpha=0.5)
ax.fill(x_wheel_left_reflected, y_wheel_left_reflected, color='black', alpha=0.5)
ax.fill(x_wheel_right_reflected, y_wheel_right_reflected, color='black', alpha=0.5)

# Add some labels and formatting to the plot
ax.set_title('House Sketch (Reflection - Origin)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])

# Show the plot
plt.show()


# DILATING BY FACTOR OF K
# Define the x and y coordinates of the House body
x_body = [-0.0, -1.0, -1.0, -0.0]
y_body = [-0.0, -0.5, -0.5, -0.0]

# Define the x and y coordinates of the House roof
x_roof = [-0.2, -0.8, -1.0, -0.0]
y_roof = [-0.5, -0.5, -0.0, -0.0]

# Define the x and y coordinates of the House House
x_wheel_left = [-0.2, -0.3, -0.3, -0.2]
y_wheel_left = [-0.0, -0.0, -0.2, -0.2]
x_wheel_right = [-0.7, -0.8, -0.8, -0.7]
y_wheel_right = [-0.0, -0.0, -0.2, -0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the original House using the fill() function
ax.fill(x_body, y_body, color='red')
ax.fill(x_roof, y_roof, color='gray')
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Multiply the x and y coordinates of all the points in the House sketch by 2 to dilate it by a factor of 2
x_body_dilated = [2 * x for x in x_body]
y_body_dilated = [2 * y for y in y_body]
x_roof_dilated = [2 * x for x in x_roof]
y_roof_dilated = [2 * y for y in y_roof]
x_wheel_left_dilated = [2 * x for x in x_wheel_left]
y_wheel_left_dilated = [2 * y for y in y_wheel_left]
x_wheel_right_dilated = [2 * x for x in x_wheel_right]
y_wheel_right_dilated = [2 * y for y in y_wheel_right]

# Plot the dilated House using the fill() function
ax.fill(x_body_dilated, y_body_dilated, color='red', alpha=0.5)
ax.fill(x_roof_dilated, y_roof_dilated, color='gray', alpha=0.5)
ax.fill(x_wheel_left_dilated, y_wheel_left_dilated, color='black', alpha=0.5)
ax.fill(x_wheel_right_dilated, y_wheel_right_dilated, color='black', alpha=0.5)

# Add some labels and formatting to the plot
ax.set_title('House Sketch (Dilation - Factor of 2)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([-3.0, 3.0])
ax.set_ylim([-3.0, 3.0])

# Show the plot
plt.show()



# REFLECTING OVER THE LINE Y=X
# Define the x and y coordinates of the House body
x_body = [-0.0, -1.0, -1.0, -0.0]
y_body = [-0.0, -0.5, -0.5, -0.0]

# Define the x and y coordinates of the House roof
x_roof = [-0.2, -0.8, -1.0, -0.0]
y_roof = [-0.5, -0.5, -0.0, -0.0]

# Define the x and y coordinates of the House House
x_wheel_left = [-0.2, -0.3, -0.3, -0.2]
y_wheel_left = [-0.0, -0.0, -0.2, -0.2]
x_wheel_right = [-0.7, -0.8, -0.8, -0.7]
y_wheel_right = [-0.0, -0.0, -0.2, -0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the original House using the fill() function
ax.fill(x_body, y_body, color='red')
ax.fill(x_roof, y_roof, color='gray')
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Swap the x and y coordinates of all the points in the House sketch to reflect it over the line y=x
x_body_reflected = y_body
y_body_reflected = x_body
x_roof_reflected = y_roof
y_roof_reflected = x_roof
x_wheel_left_reflected = y_wheel_left
y_wheel_left_reflected = x_wheel_left
x_wheel_right_reflected = y_wheel_right
y_wheel_right_reflected = x_wheel_right

# Plot the reflected House using the fill() function
ax.fill(x_body_reflected, y_body_reflected, color='red', alpha=0.5)
ax.fill(x_roof_reflected, y_roof_reflected, color='gray', alpha=0.5)
ax.fill(x_wheel_left_reflected, y_wheel_left_reflected, color='black', alpha=0.5)
ax.fill(x_wheel_right_reflected, y_wheel_right_reflected, color='black', alpha=0.5)

# Add some labels and formatting to the plot
ax.set_title('House Sketch (Reflection y=x)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])

# Show the plot
plt.show()

# ROTATION THROUGH A 43* ANGLE
#import matplotlib.pyplot as plt
import numpy as np

# Define the x and y coordinates of the House body
x_body = [-0.0, -1.0, -1.0, -0.0]
y_body = [-0.0, -0.5, -0.5, -0.0]

# Define the x and y coordinates of the House roof
x_roof = [-0.2, -0.8, -1.0, -0.0]
y_roof = [-0.5, -0.5, -0.0, -0.0]

# Define the x and y coordinates of the House House
x_wheel_left = [-0.2, -0.3, -0.3, -0.2]
y_wheel_left = [-0.0, -0.0, -0.2, -0.2]
x_wheel_right = [-0.7, -0.8, -0.8, -0.7]
y_wheel_right = [-0.0, -0.0, -0.2, -0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the original House using the fill() function
ax.fill(x_body, y_body, color='red')
ax.fill(x_roof, y_roof, color='gray')
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Define the rotation angle in radians
theta = np.radians(37)

# Define the rotation matrix
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c)))

# Apply the rotation matrix to the House coordinates
House = [x_body + x_roof + x_wheel_left + x_wheel_right, y_body + y_roof + y_wheel_left + y_wheel_right]
House_rotated = np.dot(R, House)

# Split the rotated House back into its component parts
x_body_rotated = House_rotated[0][:4]
y_body_rotated = House_rotated[1][:4]
x_roof_rotated = House_rotated[0][4:8]
y_roof_rotated = House_rotated[1][4:8]
x_wheel_left_rotated = House_rotated[0][8:12]
y_wheel_left_rotated = House_rotated[1][8:12]
x_wheel_right_rotated = House_rotated[0][12:16]
y_wheel_right_rotated = House_rotated[1][12:16]

# Plot the rotated House using the fill() function
ax.fill(x_body_rotated, y_body_rotated, color='red', alpha=0.5)
ax.fill(x_roof_rotated, y_roof_rotated, color='gray', alpha=0.5)
ax.fill(x_wheel_left_rotated, y_wheel_left_rotated, color='black', alpha=0.5)
ax.fill(x_wheel_right_rotated, y_wheel_right_rotated, color='black', alpha=0.5)

# Add some labels and formatting to the plot
ax.set_title('House Sketch (Rotation - 43 Degree Angle)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([-2.0, 2.0])
ax.set_ylim([-2.0, 2.0])

# Show the plot
plt.show()


# Original??
# Define the x and y coordinates of the car body
x_body = [-0.0, -1.0, -1.0, -0.0]
y_body = [-0.0, -0.5, -0.5, -0.0]

# Define the x and y coordinates of the car roof
x_roof = [-0.2, -0.8, -1.0, -0.0]
y_roof = [-0.5, -0.5, -0.0, -0.0]

# Define the x and y coordinates of the car wheels
x_wheel_left = [-0.2, -0.3, -0.3, -0.2]
y_wheel_left = [-0.0, -0.0, -0.2, -0.2]
x_wheel_right = [-0.7, -0.8, -0.8, -0.7]
y_wheel_right = [-0.0, -0.0, -0.2, -0.2]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the car using the fill() function
ax.fill(x_body, y_body, color='red')
ax.fill(x_roof, y_roof, color='gray')
ax.fill(x_wheel_left, y_wheel_left, color='black')
ax.fill(x_wheel_right, y_wheel_right, color='black')

# Add some labels and formatting to the plot
ax.set_title('Car Sketch')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the limits of the x and y axes
ax.set_xlim([-2.0, 2.0])
ax.set_ylim([-2.0, 2.0])

# Show the plot
plt.show()
