# sound_machine.py
# A simple script to play sounds when specific keys are pressed.

try:
    from pynput import keyboard
except ImportError as e:
    if "this platform is not supported" in str(e) or "DISPLAY" in str(e):
        print(f"Error importing pynput.keyboard: {e}")
        print("This likely means pynput cannot connect to a display server (e.g., X11).")
        print("If you are running in a headless environment, you might need to:")
        print("1. Set up a virtual display server (e.g., Xvfb).")
        print("2. Or, pynput might not be suitable for this environment without a display.")
    else:
        print(f"pynput library not found or other ImportError: {e}. Please install it using: pip install pynput")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while importing pynput: {e}")
    exit()

try:
    from playsound import playsound
except ImportError:
    print("playsound library not found. Please install it using: pip install playsound")
    exit()
except Exception as e:
    # Handle other potential playsound import errors, e.g. on Linux if GStreamer is missing
    print(f"Error importing playsound: {e}")
    print("Please ensure all dependencies for playsound are installed for your system.")
    print("For Linux, you might need to install GStreamer: sudo apt-get install python3-gst-1.0 gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0")
    exit()

# --- Configuration ---
# This dictionary will map keyboard characters to sound file paths.
# Example: sound_map = {'a': 'sounds/sound1.wav', 'b': 'sounds/sound2.mp3'}
sound_map = {
    '1': 'sounds/kick.wav',
    '2': 'sounds/snare.wav',
    '3': 'sounds/hihat_closed.wav',
    '4': 'sounds/hihat_open.wav',
    '5': 'sounds/clap.wav',
    '6': 'sounds/laser.wav',
    '7': 'sounds/explosion.wav',
    '8': 'sounds/coin.wav',
    '9': 'sounds/powerup.wav',
    '0': 'sounds/error.wav',
    'q': 'sounds/note_c4.wav',
    'w': 'sounds/note_d4.wav',
    'e': 'sounds/note_e4.wav',
    'r': 'sounds/note_f4.wav',
    't': 'sounds/note_g4.wav',
    'y': 'sounds/note_a4.wav',
    'u': 'sounds/note_b4.wav',
    'i': 'sounds/note_c5.wav',
}

# --- Keyboard Event Handlers ---

def on_press(key):
    """
    Handles key press events.
    Plays a sound if the pressed key is mapped in sound_map.
    Exits the script if the Escape key is pressed.
    """
    try:
        key_char = key.char
        if key_char and key_char in sound_map:
            sound_file = sound_map[key_char]
            print(f"Playing sound for '{key_char}': {sound_file}")
            try:
                playsound(sound_file)
            except Exception as e:
                # Catching a generic exception from playsound as specific errors can vary
                # (e.g., FileNotFoundError, playsound.PlaysoundException for various playback issues)
                print(f"Error playing sound '{sound_file}': {e}")
    except AttributeError:
        # This occurs if a special key (like Shift, Ctrl, Esc) is pressed, as they don't have a 'char' attribute.
        # We'll handle specific special keys below if needed.
        pass
    except Exception as e:
        print(f"An unexpected error occurred in on_press: {e}")

    # Check for Escape key to stop the listener
    if key == keyboard.Key.esc:
        print("Exiting Sound Machine...")
        return False  # Returning False stops the listener

def on_release(key):
    """
    Handles key release events.
    Currently does nothing.
    """
    pass

# --- Main Execution ---

if __name__ == "__main__":
    print("Sound Machine Activated.")
    print("Press mapped keys (0-9, q, w, e, r, t, y, u, i) to play sounds.")
    print("Press Esc to exit.")

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        try:
            listener.join()
        except Exception as e:
            print(f"An error occurred with the keyboard listener: {e}")

    print("Sound Machine deactivated.")
