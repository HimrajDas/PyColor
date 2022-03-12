from tkinter import *
import random
BACKGROUND_COLOR = "#BCFFB9"

colors = ["Red", "Blue", "Green", "Black", "Pink", "Yellow", "Orange", "White", "Purple", "Brown"]
score = 0
timeleft = 30

def startgame(event):
    if timeleft == 30:
        countdown()
    next_color()


def next_color():
    global score
    global timeleft
    if timeleft > 0:
        entry.focus_set()
        if entry.get().lower() == colors[1].lower():
            score += 1
        entry.delete(0, END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        score_label.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text="Time left: " + str(timeleft))
        time_label.after(1000, countdown)


window = Tk()
window.title("PyColor")
window.minsize(width=400, height=350)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=350, height=70)
canvas.create_text(
    180, 
    30, 
    width=330,
    text="Type in the color of the words, and not the words!", 
    font=("Arial", 20, "italic")
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

score_label = Label(text="Press enter to start", bg=BACKGROUND_COLOR, font=("Arial", 15, "italic"))
score_label.grid( row=1, column=0)

time_label = Label(text="Time left: " + str(timeleft), bg=BACKGROUND_COLOR, font=("Arial", 15, "italic"))
time_label.grid(row=1, column=1)

# A label to display colors
label = Label(bg=BACKGROUND_COLOR, font=("Arial", 25, "italic"))
label.grid(row=2, column=0, columnspan=2)

entry = Entry(width=40)
window.bind("<Return>", startgame)
entry.grid(row=3, column=0, columnspan=2)
entry.focus_set()

window.mainloop()
