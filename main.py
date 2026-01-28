import random, keyboard, os

DICE_ART = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘")
}
print("Press Enter to roll. Press Shift to stop rolling and exit.")

def roll():
    result = random.randint(1, 6)
    print(f"Result: {result}")
    for row in DICE_ART[result]:
        print(row)

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'shift':
            print("Exiting...")
            break
        elif event.name == 'enter':
            roll()
