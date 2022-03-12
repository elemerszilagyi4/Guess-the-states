import turtle
import pandas

screen = turtle.Screen()

data = pandas.read_csv("50_states.csv")

states = data["state"].tolist()
xcor = data["x"].tolist()
ycor = data["y"].tolist()

screen.title("Guess the state")

okay = 0

screen.bgpic("blank_states_img.gif")

guessed_states = []

while okay != 50:
    user_input = screen.textinput(f"{okay}/50 states guessed.", "Guess another state\nType exit if you want to quit!").title()
    if user_input.title() in states:
        okay += 1
        guessed_states.append(user_input)
        index = states.index(user_input)
        guessed = turtle.Turtle()
        guessed.penup()
        guessed.hideturtle()
        guessed.goto((xcor[index], ycor[index]))
        guessed.write(f"{user_input}", align="center", font=("Arial", 12, "normal"))
    elif user_input == "Exit":
        break

not_guessed = []

for state in states:
    if state not in guessed_states:
        not_guessed.append(state)

not_guessed_cont = {"state": not_guessed}

new_df = pandas.DataFrame(not_guessed_cont)

new_df.to_csv("You have to learn these states.csv")