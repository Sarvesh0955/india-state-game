import turtle
import pandas

screen = turtle.Screen()
screen.title("State Game")

image = "./India-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./states_data.csv")
state_name = data["state"].tolist()
state_x_cor = data["x"].tolist()
state_y_cor = data["y"].tolist()
state_dict = {}

TOTAL_STATE = len(state_name)

for i in range(TOTAL_STATE):
    state_dict[state_name[i]] = (state_x_cor[i], state_y_cor[i])

count = 0
game_is_one = True
tur = turtle.Turtle()
tur.hideturtle()
tur.penup()
guessed_state = []

while game_is_one:
    answer = screen.textinput(title=f"Guess the State {count}/{TOTAL_STATE}", prompt="What is another state name?").title()
    if answer in state_dict and answer not in guessed_state:
        tur.goto(state_dict[answer])
        tur.write(answer)
        count += 1
        guessed_state.append(answer)

    if count == TOTAL_STATE:
        game_is_one = False

screen.exitonclick()
