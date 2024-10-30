import turtle
import random

# Register the custom shape
turtle.register_shape("./gif/boss.gif")

class Boss:
    def __init__(self, x, y):
        self.health = 100  # Boss health
        self.size = 5  # Number of spikes around the boss
        self.move_direction = 1  # Movement direction: 1 for right, -1 for left
        self.pen = turtle.Turtle()
        self.pen.hideturtle()  # Hide the pen initially
        self.pen.penup()
        self.restart = False

        # Initialize the main body
        self.body = turtle.Turtle()
        self.body.shape("./gif/boss.gif")
        self.body.penup()
        self.body.goto(x, y)
        self.body.shapesize(stretch_wid=3, stretch_len=3)  # Body size

    def move(self):
        # Move the boss in a zigzag pattern
        new_x = self.body.xcor() + 5 * self.move_direction
        self.body.setx(new_x)

        # Reverse direction at screen edges
        if self.body.xcor() > 230 or self.body.xcor() < -230:
            self.move_direction *= -1  # Reverse direction
            new_y = self.body.ycor() - 10  # Move down
            self.body.sety(new_y)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.defeated()
        elif self.health < 15:
            self.appear_randomly()
        elif self.health < 25:
            self.move()
        elif self.health < 50:
            self.appear_randomly()
        elif self.health < 70:
            self.move()
        elif self.health < 90:
            self.move()

    def appear_randomly(self):
        # Move the boss to a random position on the screen
        new_x = random.randint(-250, 220)  # Random x position within bounds
        new_y = random.randint(-100, 170)  # Random y position in the top half only
        self.body.goto(new_x, new_y)  # Update position of the boss

    def defeated(self):
        self.restart = True
        self.body.hideturtle()  # Hide the boss on defeat

        # Display boss defeated message
        self.pen.goto(0, 0)
        self.pen.color("red")
        self.pen.write("Boss Defeated!", align="center", font=("Courier", 28, "bold"))

        # Schedule the next step instead of using sleep
        turtle.ontimer(self.display_final_message, 2000)  # Show final message after 2 seconds

    def display_final_message(self):
        self.pen.clear()  # Clear the previous message
        self.pen.color("green")
        self.pen.write("Thanks For Playing!", align="center", font=("Courier", 28, "bold"))
        turtle.ontimer(self.restart_message, 2000)  # Show restart message after 2 seconds

    def is_defeated(self):
        # Check if the boss has moved below the screen threshold
        return self.body.ycor() < -230

    def restart_message(self):
        self.pen.clear()  # Clear the previous message
        self.pen.color("white")
        self.pen.write("Press 'R' to play again!", align="center", font=("Courier", 28, "bold"))
