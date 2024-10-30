import turtle
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.round = 1
        self.bullets_available = 100
        self.initial_bullets = 100
        self.boss_health = 0  # Initialize boss health
        self.boss_health_displayed = False  # Initialize the boss health display status
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.setposition(-280, 260)
        self.update_score() # Initial score display
        self.set_bullets()

    def update_score(self):
        self.pen.clear()  # Clear previous display
        self.pen.write(
            f"🏆 Score: {self.score}  🎮 Round: {self.round}  🔫 Bullets: {self.bullets_available}",
            align="left", font=("Courier", 14, "normal")
        )

        # If boss is active, show the boss health
        if self.boss_health_displayed:
            self.pen.clear()
            self.pen.goto(-230, 240)  # Set position for boss health display
            self.pen.color("gold")  # Change color for boss health
            self.pen.write(
                f"💚 Boss Health: {self.boss_health}  | 🔫 Bullets: {self.bullets_available}\n"
                                     "\t  Aim for the center!",
                align="left",
                font=("Courier", 16, "bold")
            )
    def increase_score(self, points=10):
        self.score += points
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.round = 1
        self.bullets_available = self.initial_bullets
        self.boss_health_displayed = False  # Reset boss health display
        self.update_score()

    def set_final_round(self, health):
        self.boss_health = health  # Store boss health
        self.boss_health_displayed = True  # Indicate that boss health is displayed
        self.update_score()  # Update score to reflect boss health

    def decrement_health(self):
        self.boss_health -= 10
    def next_round(self):
        self.round += 1
        self.increase_bullets()
        self.set_bullets()
        self.update_score()

    def set_bullets(self):
        self.bullets_available = self.initial_bullets

    def increase_bullets(self):
        self.initial_bullets += 10

    def decrement_bullets(self):
        if self.bullets_available > 0:
            self.bullets_available -= 1
        self.update_score()
