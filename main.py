import random, keyboard, tkinter as tk

def roll_dice(event=None):
    dice_symbols = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }

    result = random.randint(1, 6)

    label_dice.config(text=dice_symbols[result])
    label_status.config(text=f"Result: {result}")

def close_app(event=None):
    root.destroy()

root = tk.Tk()
root.title("Dice Game")
root.geometry("300x300")

label_dice = tk.Label(root, text="🎲", font=("Helvetica", 120))
label_dice.pack(pady=20)

label_status = tk.Label(root, text="Press Enter to roll", font=("Arial", 12))
label_status.pack()

label_hint = tk.Label(root, text="Press Escape to exit", font=("Arial", 10), fg="blue")
label_hint.pack(side="bottom", pady=10)

root.bind("<Return>", roll_dice)
root.bind("<Escape>", close_app)

root.mainloop()
