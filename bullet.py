import turtle
class Bullet:
    def __init__(self):
        self.bullet = turtle.Turtle()
        self.bullet.shape("square")
        self.bullet.color("red")
        self.bullet.penup()
        self.bullet.speed(0)
        self.bullet.setheading(90)
        self.bullet.shapesize(stretch_wid=0.2, stretch_len=0.5)
        self.bullet.hideturtle()
        self.speed = 20
        self.state = "ready"  # "ready" or "fire"

    def fire(self, x, y):
        if self.state == "ready":
            self.state = "fire"
            self.bullet.setposition(x, y + 10)
            self.bullet.showturtle()

    def move(self):
        if self.state == "fire":
            y = self.bullet.ycor()
            y += self.speed
            self.bullet.sety(y)
            if self.bullet.ycor() > 275:
                self.reset()

    def reset(self):
        self.bullet.hideturtle()
        self.state = "ready"

    def is_off_screen(self):
        # Return True if the bullet is off the screen (above or below)
        return self.bullet.ycor() > 275 or self.bullet.ycor() < -275