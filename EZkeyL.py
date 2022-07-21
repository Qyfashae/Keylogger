import keyboard

keys = keyboard.record(until="KILL COMMAND")  # Change KC
keyboard.play(keys)  # Change to work within a RS or BS
