import turtle, pandas

data = pandas.read_csv("indianStates/29+7_states.csv")

screen = turtle.Screen()
screen.title("India States Game")

image = "indianStates/blank_states_map.gif"
screen.addshape(image)

turtle.shape(image)

correct_guesses = []
score = 0
total_score = len(data["state"])

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/{total_score} States Correct", prompt="What's another state name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in data["state"].to_list():
        correct_guesses.append(answer_state)
        city = turtle.Turtle()
        city.hideturtle()
        city.penup()
        x = data[data["state"] == answer_state]["x"].to_list()[0]
        y = data[data["state"] == answer_state]["y"].to_list()[0]
        city.goto(x, y)
        city.write(answer_state, align="center", font=("Arial", 8, "normal"))
        score += 1
        if score == total_score:
            game_is_on = False

incorrect_guesses = [state for state in data["state"].to_list() if state not in correct_guesses]
pandas.DataFrame(incorrect_guesses).to_csv("indianStates/states_to_learn.csv")