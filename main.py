import turtle
import threading
import time
from player import Player
from enemy import Enemy
from bullet import Bullet
from boss import Boss
from scoreboard import Scoreboard

# ASCII Art for Loader
loader_art = r"""
  _________                                              
 /   _____/______ _____     ____   ____                  
 \_____  \ \____ \\__  \  _/ ___\_/ __ \                
 /        \|  |_> >/ __ \_\  \___\  ___/                
/_______  /|   __/(____  / \___  >\___  >               
        \/ |__|        \/      \/     \/                

.___                           .___                     
|   |  ____ ___  _______     __| _/ ____ _______  ______
|   | /    \\  \/ /\__  \   / __ |_/ __ \\_  __ \/  ___/
|   ||   |  \\   /  / __ \_/ /_/ |\  ___/ |  | \/\___ \ 
|___||___|  / \_/  (____  /\____ | \___  >|__|  /____  >
          \/            \/      \/     \/            \/ 
"""

# Set up the screen
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgpic("./gif/back.gif")
screen.setup(width=600, height=600)
screen.tracer(0)

# Global variables for blinking text control
blink_on = True
enter_writer = None
Hard = False
Medium = False
Easy = False

# Function to display blinking text
def display_blinking_text():
    global blink_on
    while blink_on:
        enter_writer.clear()
        enter_writer.color("green")
        enter_writer.goto(0,-230)
        enter_writer.write(
            '"Press 1 for Easy, 2 for Medium, or 3 for Hard to Start\n\n'
            '\t    ➡️ Use Arrow Keys to Move\n\n'
            '\t    Press Space to Shoot\n\n'
            '\t    🔄 Total Rounds: Four"',
            align='center', font=("Courier", 12, "bold")
        )
        time.sleep(0.7)
        enter_writer.clear()
        time.sleep(0.2)

# Show loader screen with blinking text
def show_loader_screen():
    global enter_writer
    loader_writer = turtle.Turtle()
    loader_writer.speed(0)
    loader_writer.color("white")
    loader_writer.penup()
    loader_writer.hideturtle()
    loader_writer.setposition(10, -80)
    loader_writer.write(loader_art, align="center", font=("Courier", 10, "normal"))

    enter_writer = turtle.Turtle()
    enter_writer.speed(0)
    enter_writer.color("white")
    enter_writer.penup()
    enter_writer.hideturtle()
    enter_writer.setposition(8, -107)

    blink_thread = threading.Thread(target=display_blinking_text)
    blink_thread.start()

    screen.listen()
    screen.onkeypress(lambda: start_game(1), "1")
    screen.onkeypress(lambda: start_game(2), "2")
    screen.onkeypress(lambda: start_game(3), "3")


# Press "Enter" to start
def start_game(level):
    global blink_on
    blink_on = False
    enter_writer.clear()
    screen.clearscreen()

    screen.bgpic('./gif/sb.png')
    screen.setup(width=600, height=600)
    screen.tracer(0)

    global player, current_level , boss_round, enemies, bullets, scoreboard, current_round, enemies_per_round,shape, current_shape_index
    player = Player()
    enemies = []
    bullets = []
    scoreboard = Scoreboard()
    scoreboard.set_bullets()

    current_level = level
    current_round = 1

    if level == 1:
        enemies_per_round = 10
    elif level == 2:
        enemies_per_round = 15
    elif level == 3:
        enemies_per_round = 20
    else:
        pass

    boss_round = 1

    current_shape_index = 0

    def spawn_enemies():
        global current_shape_index
        shapes = ["./gif/enemy.gif", "./gif/enemy02.gif", "./gif/enemy03.gif", "./gif/enemy04.gif", "./gif/enemy05.gif"]
        enemies = []
        for i in range(enemies_per_round):
            row = i // 10  # 10 enemies per row
            col = i % 10
            shape = shapes[current_shape_index]
            enemies.append(Enemy(-200 + col * 50, 200 - row * 30, shape))  # Adjust the vertical position
            current_shape_index = (current_shape_index + 1) % len(shapes)
        return enemies

    def is_collision(t1, t2):
        return t1.distance(t2) < 15

    def boss_is_collision(t1, t2):
        return t1.distance(t2) < 20

    def fire_bullet():
        current_bullets = len(bullets)
        number_of_bullets = scoreboard.bullets_available

        if current_bullets < number_of_bullets:
            bullet = Bullet()
            bullet.fire(player.player.xcor(), player.player.ycor())
            bullets.append(bullet)
            scoreboard.decrement_bullets()

    def game_over():
        game_over_writer = turtle.Turtle()
        game_over_writer.hideturtle()
        game_over_writer.penup()
        game_over_writer.color("red")
        game_over_writer.goto(0, 0)
        game_over_writer.write("Game Over! Press 'r' to restart", align="center", font=("Courier", 24, "bold"))
        screen.update()
        time.sleep(2)
        turtle.done()

    def out_of_bullets():
        out_of_bullets_writer = turtle.Turtle()
        out_of_bullets_writer.hideturtle()
        out_of_bullets_writer.penup()
        out_of_bullets_writer.color("red")
        out_of_bullets_writer.goto(0, 0)
        out_of_bullets_writer.write("Out of Bullets!", align="center", font=("Courier", 24, "bold"))
        out_of_bullets_writer.goto(0, -30)
        out_of_bullets_writer.write("Press 'R' to restart", align="center", font=("Courier", 20, "normal"))

        screen.update()
        time.sleep(2)
        turtle.done()

    def reset_game():
        global player, enemies, bullets, scoreboard, current_round, enemies_per_round
        screen.clearscreen()
        start_game(current_level)

    screen.listen()
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")
    screen.onkeypress(fire_bullet, "space")


    enemies.extend(spawn_enemies())
    boss = None

    while True:
        time.sleep(0.02)
        screen.update()





        if current_round > boss_round and not boss:

            boss = Boss(0, 170)
            for enemy in enemies:
                enemy.enemy.hideturtle()  # Hide all enemies
            scoreboard.set_final_round(boss.health)  # Set boss health (example value)
            enemies.clear()
             # Spawn the boss
            scoreboard.bullets_available += 5

 # Give extra bullets for the boss fight

        if boss:
            scoreboard.boss_health_displayed = True
            scoreboard.update_score()  # Update scoreboard for boss health
            boss.move()

            if boss.is_defeated():
                screen.onkeypress(reset_game, "r")
                game_over()  # Game over if an enemy goes off-screen


        if not boss:
            for enemy in enemies:
                enemy.move()
                if enemy.enemy.ycor() < -240:
                    screen.onkeypress(reset_game, "r")
                    game_over()  # Game over if an enemy goes off-screen

        bullets_to_remove = []
        for bullet in bullets:
            bullet.move()
            if bullet.is_off_screen():
                bullets_to_remove.append(bullet)

            if not boss:
                for enemy in enemies:
                    if is_collision(bullet.bullet, enemy.enemy):
                        bullet.reset()
                        enemy.delete_enemy()
                        enemies.remove(enemy)
                        scoreboard.increase_score()
                        bullets_to_remove.append(bullet)
                        break

            if boss:
                # Check collision directly with the boss's body
                if boss_is_collision(bullet.bullet, boss.body):
                    bullet.reset()
                    bullets_to_remove.append(bullet)
                    boss.take_damage(10)
                    scoreboard.decrement_health()  # Boss takes damage

                    if boss.health <= 0:
                        if boss.restart:
                            # Disable key press functionality initially
                            screen.onkeypress(None, "r")  # Unbind the key press

                            # Function to enable key press after delay
                            def enable_key_press():
                                screen.onkeypress(reset_game, "r")  # Bind the key press to reset_game

                            # Call enable_key_press after 4000 milliseconds (4 seconds)
                            turtle.ontimer(enable_key_press, 4000)

                        boss.defeated()  # Handle boss defeat
                        scoreboard.boss_health_displayed = False  # Reset boss health display
                        current_round += 1  # Go to the next round
                        break

        for bullet in bullets_to_remove:
            bullets.remove(bullet)

        if scoreboard.bullets_available == 0 and all(bullet.is_off_screen() for bullet in bullets):
            screen.onkeypress(reset_game, "r")
            out_of_bullets()
          # Handle out of bullets scenario

        if not enemies and boss is None:
            scoreboard.next_round()  # Prepare for the next round
            enemies_per_round += 10  # Increase number of enemies for the next round
            enemies.extend(spawn_enemies())  # Spawn new enemies
            current_round += 1
            # Move to the next round


show_loader_screen()
screen.mainloop()
