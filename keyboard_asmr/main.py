import pygame
import keyboard

# Initialize pygame mixer
pygame.mixer.init()

# Locate the sound
path1 = "mech_keyboard.mp3"
path2 = "quack.mp3"

sound_path = path2 # Replace with your sound file path
sound = pygame.mixer.Sound(sound_path)

def play_sound(event):
    sound.play()

def main():
    # Listen for all key events
    keyboard.on_press(play_sound)

    # Keep the script running
    print("Press any key to play the sound. Press 'Esc' to exit.")
    keyboard.wait('esc')
    print("Exiting...")

if __name__ == "__main__":
    main()
