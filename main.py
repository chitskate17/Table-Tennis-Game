import turtle
import time
import winsound

# create the screen
screen1 = turtle.Screen()
screen1.title("Table Tennis")

screen1.bgpic("assets/background.gif")
screen1.setup(width=1050, height=650)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("Red")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("Blue")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)

# Table tennis ball shape
pong_ball = turtle.Turtle()
pong_ball.speed(45)
pong_ball.shape("circle")
pong_ball.color("White")
pong_ball.penup()
pong_ball.goto(0, 0)
pong_ball.dx = 5
pong_ball.dy = -5


# creating functions to move the paddles vertically
def paddle_L_up():
    y = left_paddle.ycor()
    if y < 230:
        y += 20
    left_paddle.sety(y)


def paddle_L_down():
    y = left_paddle.ycor()
    if y > -230:
        y -= 20
    left_paddle.sety(y)


def paddle_R_up():
    y = right_paddle.ycor()
    if y < 230:
        y += 20
    right_paddle.sety(y)


def paddle_R_down():
    y = right_paddle.ycor()
    if y > -230:
        y -= 20
    right_paddle.sety(y)


def play_ball_hit_sound():
    winsound.PlaySound("assets/ping-pong-sound2.wav", winsound.SND_ASYNC)


def play_oh_no_sound():
    winsound.PlaySound("assets/oh no sound effect.wav", winsound.SND_ASYNC)


def flash_ball():
    pong_ball.color("Yellow")
    screen1.update()
    time.sleep(0.05)
    pong_ball.color("White")


def win_animation(who_won):
    if who_won == 'left_player':
        for _ in range(36):
            if left_paddle.ycor() < 230 and right_paddle.ycor() > -230:
                left_paddle.sety(left_paddle.ycor() + 2)
                right_paddle.sety(right_paddle.ycor() - 2)
                pong_ball.right(10)
                screen1.update()
                time.sleep(0.02)

    if who_won == 'right_player':
        for _ in range(36):
            if left_paddle.ycor() > -230 and right_paddle.ycor() < 230:
                left_paddle.sety(left_paddle.ycor() - 2)
                right_paddle.sety(right_paddle.ycor() + 2)
                pong_ball.right(10)
                screen1.update()
                time.sleep(0.02)


def increase_speed():
    if abs(pong_ball.dx) < 10:
        pong_ball.dx *= 1.05
        pong_ball.dy *= 1.05


def show_instructions():
    # display instructions for controls
    instruction = turtle.Turtle()
    instruction.speed(0)
    instruction.color("White")
    instruction.penup()
    instruction.hideturtle()
    instruction.goto(0, 220)
    instruction.write("Player 1: W/S | Player 2: Up/Down", align='center', font=('Times New Roman', 18, 'normal'))
    instruction.goto(0,180)
    instruction.write("Press Space To Start", align='center', font=("Times New Roman", 18, 'normal'))

    # bind the space bar to start the game
    screen1.listen()
    screen1.onkeypress(lambda: [instruction.clear(), run_game()], "space")


def reset_game():
    pong_ball.goto(0, 0)
    pong_ball.dx = 5
    pong_ball.dy = -5
    screen1.listen()
    screen1.onkeypress(paddle_L_up, 'w')
    screen1.onkeypress(paddle_L_down, 'x')
    screen1.onkeypress(paddle_R_up, 'Up')
    screen1.onkeypress(paddle_R_down, 'Down')


def run_game():
    # initialize score of players
    left_player = 0
    right_player = 0

    # display the score
    screen_display = turtle.Turtle()
    screen_display.speed(0)
    screen_display.color("Dark blue")
    screen_display.penup()
    screen_display.hideturtle()
    screen_display.goto(0, 280)
    screen_display.write("Left Player: 0   Right Player: 0", align='center', font=('Times New Roman', 24, 'normal'))

    # set the binding of keys to move the paddle up or down
    screen1.listen()
    screen1.onkeypress(paddle_L_up, 'w')
    screen1.onkeypress(paddle_L_down, 'x')
    screen1.onkeypress(paddle_R_up, 'Up')
    screen1.onkeypress(paddle_R_down, 'Down')

    winning_score = 5  # the score to win the game

    try:
        while True:

            screen1.update()
            pong_ball.setx(pong_ball.xcor() + pong_ball.dx)
            pong_ball.sety(pong_ball.ycor() + pong_ball.dy)

            # check all the borders
            if pong_ball.ycor() > 280:
                pong_ball.sety(280)
                pong_ball.dy *= -1

            if pong_ball.ycor() < -280:
                pong_ball.sety(-280)
                pong_ball.dy *= -1

            if pong_ball.xcor() > 500:
                play_oh_no_sound()
                pong_ball.goto(0, 0)
                pong_ball.dx = 5
                pong_ball.dy = -5
                pong_ball.dy *= -1
                left_player += 1
                screen_display.clear()
                screen_display.write("Left Player: {}  Right Player: {}".format(left_player, right_player),
                                     align='center',
                                     font=('Times New Roman', 24, 'normal'))

            if pong_ball.xcor() < -500:
                play_oh_no_sound()
                pong_ball.goto(0, 0)
                pong_ball.dx = 5
                pong_ball.dy = -5
                pong_ball.dy *= -1
                right_player += 1
                screen_display.clear()
                screen_display.write("Left Player: {}  Right Player: {}".format(left_player, right_player),
                                     align='center',
                                     font=('Times New Roman', 24, 'normal'))

            # collision of ball and paddles
            if (pong_ball.xcor() > 360 and pong_ball.xcor() < 370) and (
                    right_paddle.ycor() + 80 > pong_ball.ycor() > right_paddle.ycor() - 80):
                pong_ball.setx(360)
                pong_ball.dx *= -1
                flash_ball()
                increase_speed()
                play_ball_hit_sound()

            if (pong_ball.xcor() < -360 and pong_ball.xcor() > -370) and (
                    left_paddle.ycor() + 80 > pong_ball.ycor() > left_paddle.ycor() - 80):
                pong_ball.setx(-360)
                pong_ball.dx *= -1.1
                flash_ball()
                increase_speed()
                play_ball_hit_sound()

            if left_player == winning_score:
                screen_display.clear()
                win_animation('left_player')
                screen_display.write("Left Player Wins!", align='center', font=('Times New Roman', 24, 'normal'))
                time.sleep(3)
                play_again = screen1.textinput("Game Over!", "Play Again? (Yes/No)")
                if play_again.lower() == 'yes':
                    reset_game()
                    left_player = 0
                    right_player = 0
                    screen_display.clear()
                    screen_display.write("Left Player: {}  Right Player: {}".format(left_player, right_player),
                                         align='center',
                                         font=('Times New Roman', 24, 'normal'))
                else:
                    turtle.bye()
                    break
            if right_player == winning_score:
                screen_display.clear()
                win_animation('right_player')
                screen_display.write("Right Player Wins!", align='center', font=('Times New Roman', 24, 'normal'))
                time.sleep(3)
                play_again = screen1.textinput("Game Over", "Play Again? (Yes/No)")
                if play_again.lower() == 'yes':
                    reset_game()
                    left_player = 0
                    right_player = 0
                    screen_display.clear()
                    screen_display.write("Left Player: {}  Right Player: {}".format(left_player, right_player),
                                         align='center',
                                         font=('Times New Roman', 24, 'normal'))
                else:
                    turtle.bye()
                    break
    except Exception as e:
        print(f"An error occurred: {e}")
        turtle.bye()


# display the game instructions
show_instructions()
turtle.mainloop()
