import turtle
turtle.register_shape('./gif/enemy.gif')
turtle.register_shape('./gif/enemy02.gif')
turtle.register_shape('./gif/enemy03.gif')
turtle.register_shape('./gif/enemy04.gif')
turtle.register_shape('./gif/enemy05.gif')

class Enemy:
    def __init__(self, x, y,shape):
        self.enemy = turtle.Turtle()
        self.enemy.shape(shape)  # Change shape to square
        self.enemy.color("green")
        self.enemy.penup()
        self.enemy.speed(0)
        self.enemy.setposition(x, y)
        self.speed = 3
        self.increase_speed(0.001)


    def move(self):
        x = self.enemy.xcor()
        x += self.speed
        self.enemy.setx(x)
        # Reverse direction and move down if it reaches the screen boundary
        if x > 250 or x < -250:
            self.speed *= -1
            y = self.enemy.ycor()
            y -= 100
            self.enemy.sety(y)

    def reset_position(self):
        self.enemy.setposition(-200, 250)

    def is_defeated(self):
        # Check if the enemy has moved below the bottom of the screen
        return self.enemy.ycor() < -245  # Adjust this value as needed for your game

    def delete_enemy(self):
        self.enemy.hideturtle()  # Hide the turtle graphic
        self.enemy.goto(1000, 1000)

    def increase_speed(self, increment=0.7):
        """Increase the speed of the enemy by a specified increment."""
        self.speed += increment