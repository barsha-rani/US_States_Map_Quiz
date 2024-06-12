import turtle
import pandas


ALIGNMENT = "center"
FONT = ("Helvetica", 8, "normal")
STATES = 50
screen = turtle.Screen()
screen.title("US States game")
IMAGE = "day-25-us-states-game-start/blank_states_img.gif"

screen.addshape(IMAGE)
turtle.shape(IMAGE)


# def play_game(answer_state, score):
#     continue_game = True
#
#     while continue_game:
#
#         timmy = turtle.Turtle()
#         timmy.hideturtle()
#         data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
#
#         state_name = data[data["state"].str.lower() == answer_state]
#
#         if state_name.empty:
#             answer_state = screen.textinput(title=f"{score}/{STATES} correct", prompt="What's another state's name")
#             play_game(answer_state, score)
#         else:
#             us_state = state_name.state.item()
#             print(us_state)
#             x = state_name.x
#             y = state_name.y
#             timmy.penup()
#             timmy.goto(int(x), int(y))
#             timmy.hideturtle()
#             timmy.write(us_state, font=FONT)
#             score += 1
#             answer_state = screen.textinput(title=f"{score}/{STATES} correct", prompt="What's another state's name")
#             if score == 50:
#                 break
#
#
# continue_game = True
# answer_state = screen.textinput(title="Guess the State", prompt="What's the state's name")
# score = 0
#
# while continue_game:
#     play_game(answer_state, score)
#     if score == 50:
#         continue_game = False
#
#
#
# play_game(answer_state, score)

# -----------------------xxxxxxxxx----------------------------------------------


# answer_state = screen.textinput(title="Guess the State", prompt="What's the state's name")
data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
all_states = data["state"].tolist()

guessed_states = []
score = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} /50 states Correct",
                                    prompt="What's the state's name").title()
    if answer_state.lower() == 'exit':
        missing_states = [states for states in all_states if states not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("notGuessed.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_name = data[data["state"] == answer_state]
        timmy.goto(int(state_name.x), int(state_name.y))
        timmy.write(answer_state, font=FONT)

#
# def check_subset(list1, list2):
#     # Convert lists to sets for efficient subset checking
#     set1 = set(list1)
#     set2 = set(list2)
#
#     # Check if list1 is a subset of list2
#     # if set1.issubset(set2):
#     #     print("list1 is a subset of list2")
#     # else:
#         # Find the items in list1 that are not in list2
#     difference = set1 - set2
#     print("list1 is not a subset of list2")
#     print("Items in list1 not present in list2:", difference)
#     df = pandas.DataFrame(difference)
#     df.to_csv("newfile.csv")


# Example usage




turtle.mainloop()
# screen.exitonclick()
