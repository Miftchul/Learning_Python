import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.title("Rose Animation")  # Set window title

# Setup turtle
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest
pen.width(2)  # Set the pen width
pen.hideturtle()  # Hide the turtle cursor for a cleaner look

# Function to draw a rose with smoother petals
def draw_rose():
    pen.color("red")  # Set the pen color to red
    pen.up()  # Lift the pen to move without drawing
    pen.goto(0, 0)  # Move to the center of the screen
    pen.down()  # Put the pen down to start drawing
    pen.begin_fill()  # Start filling the shape with color
    for i in range(3600):  # Increase the resolution for smoother petals
        angle = math.radians(i / 10)  # Convert degrees to radians with finer steps
        x = 200 * math.sin(4 * angle) * math.cos(angle)  # Parametric equation for x
        y = 200 * math.sin(4 * angle) * math.sin(angle)  # Parametric equation for y
        pen.goto(x, y)  # Move the pen to the calculated position
    pen.end_fill()  # End filling the shape

# Function to draw the stem with a gradient effect
def draw_stem():
    pen.up()  # Lift the pen to move without drawing
    pen.goto(0, -200)  # Move to the starting position of the stem
    pen.down()  # Put the pen down to start drawing
    pen.width(10)  # Set the pen width for the stem
    for i in range(30):  # Create a gradient effect with 30 steps
        pen.color(0, i / 30, 0)  # Gradient from dark green to light green
        pen.forward(10)  # Move forward to draw the stem

# Function to draw a leaf with more detail
def draw_leaf(x, y, angle):
    pen.up()  # Lift the pen to move without drawing
    pen.goto(x, y)  # Move to the starting position of the leaf
    pen.down()  # Put the pen down to start drawing
    pen.setheading(angle)  # Set the direction of the leaf
    pen.color("green")  # Set the pen color to green
    pen.begin_fill()  # Start filling the leaf with color
    for _ in range(2):  # Draw two arcs to form the leaf
        pen.circle(50, 90)  # Draw an arc with radius 50 and angle 90 degrees
        pen.left(90)  # Turn left by 90 degrees
    pen.end_fill()  # End filling the leaf

# Function to animate the drawing
def animate():
    pen.up()  # Lift the pen to move without drawing
    pen.goto(0, 0)  # Move to the center of the screen
    pen.down()  # Put the pen down to start drawing
    draw_rose()  # Draw the rose
    draw_stem()  # Draw the stem
    draw_leaf(-50, -300, 45)  # Draw the left leaf
    draw_leaf(50, -300, 135)  # Draw the right leaf

# Run the animation
animate()

# Keep the window open until the user closes it
screen.mainloop()