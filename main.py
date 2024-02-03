import turtle
import pandas
import subprocess

screen = turtle.Screen()
screen.title("Guess The States")
image = "us_map.gif"
screen.setup(width=700, height=490)
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_guessed = []

while len(states_guessed) < 50:
    user_guess = screen.textinput(title=f"{len(states_guessed)}/50 States Guessed",
                                   prompt="Enter State name or 'Exit' to quit. ").title()
    if user_guess == "Exit":
        missed_states = [state for state in all_states if state not in states_guessed]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        subprocess.run(["open", "states_to_learn.csv"])
        break
    if user_guess in all_states and user_guess not in states_guessed:
        states_guessed.append(user_guess)
        floof = turtle.Turtle()
        floof.up()
        floof.hideturtle()
        # Original way I first got it to work
        # new_x = data[data.state == user_guess].x.item()
        # new_y = data[data.state == user_guess].y.item()
        # floof.goto(new_x, new_y)
        state_data = data[data.state == user_guess]
        floof.goto(int(state_data.x), int(state_data.y))
        floof.write(user_guess, align="center", font=("Arial", 12, "bold"))
        





# print(data[data.state == "Alabama"].x[0], data[data.state == "Alabama"].y[0])

