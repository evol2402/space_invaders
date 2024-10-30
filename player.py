import turtle
turtle.register_shape("./gif/ship_resized.gif")
class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("./gif/ship_resized.gif")
        self.player.color("white")
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0, -250)
        self.player.setheading(90)
        self.speed = 15

    def move_left(self):
        x = self.player.xcor()
        x -= self.speed
        if x < -280:
            x = -280
        self.player.setx(x)

    def move_right(self):
        x = self.player.xcor()
        x += self.speed
        if x > 280:
            x = 280
        self.player.setx(x)
