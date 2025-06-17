# conda activate allpy310+-

# pip install keyboard

import keyboard


def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key {event.name} pressed")
    elif event.event_type == keyboard.KEY_UP:
        print(f"Key {event.name} released")


keyboard.hook(on_key_event)
keyboard.wait('esc')

