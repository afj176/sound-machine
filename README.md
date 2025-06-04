# Terminal Sound Machine

**Description:** A fun, terminal-based sound machine that plays sounds when you press keys.

**Features:**
*   Play sounds directly from your terminal.
*   Mapped to keyboard keys for easy triggering.
*   Supports a variety of sound types (drum beats, sound effects, musical notes).
*   Easy to customize by adding your own sound files.
*   Exit cleanly using the 'Esc' key.

**Requirements:**
*   Python 3.6+
*   `pynput` library (for keyboard input).
*   `playsound` library (for sound playback).
*   **Note on `pynput`**: This library generally requires a running display server (like X11 on Linux, or Quartz on macOS) to capture global keyboard events, even if you are only using a terminal. It may not work in truly headless environments without appropriate configuration (e.g., Xvfb or ensuring a non-display backend is used if available).
*   **Note on `playsound`**: On Linux, `playsound` may require GStreamer and its Python bindings. On macOS, it uses AppKit, and on Windows, it uses the MCI.

**Installation:**
1.  Clone this repository (or download the files).
2.  Navigate to the project directory.
3.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  **System Dependencies:**
    *   **Linux:** You might need to install system packages for `pynput` and `playsound`. For `pynput` (and its dependency `evdev`): `sudo apt-get install python3-dev libudev-dev gcc`. For `playsound` (GStreamer): `sudo apt-get install python3-gst-1.0 gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly`. (Adjust package names based on your distribution).
    *   **macOS/Windows:** `pip` should handle most things. `pynput` might require specific permissions on macOS (e.g., Accessibility access for input monitoring).

**Usage:**
1.  **Add your sounds!** Place your `.wav` or `.mp3` sound files into the `sounds/` directory. The script is pre-configured to look for specific filenames (see Key Mapping below). Make sure your files match these names, or update the `sound_map` in `sound_machine.py`.
    *(The current files in `sounds/` are placeholders and will not make noise.)*
2.  Run the script from the project's root directory:
    ```bash
    python sound_machine.py
    ```
3.  The terminal will show a message similar to: "Sound Machine Activated. Press mapped keys (0-9, q, w, e, r, t, y, u, i) to play sounds. Press Esc to exit."
4.  Press the mapped keys to play sounds.
5.  Press 'Esc' to exit.

**Key Mapping:**
The following keys are mapped to sound files in the `sounds/` directory:
```
'1': 'sounds/kick.wav'
'2': 'sounds/snare.wav'
'3': 'sounds/hihat_closed.wav'
'4': 'sounds/hihat_open.wav'
'5': 'sounds/clap.wav'
'6': 'sounds/laser.wav'
'7': 'sounds/explosion.wav'
'8': 'sounds/coin.wav'
'9': 'sounds/powerup.wav'
'0': 'sounds/error.wav'
'q': 'sounds/note_c4.wav'
'w': 'sounds/note_d4.wav'
'e': 'sounds/note_e4.wav'
'r': 'sounds/note_f4.wav'
't': 'sounds/note_g4.wav'
'y': 'sounds/note_a4.wav'
'u': 'sounds/note_b4.wav'
'i': 'sounds/note_c5.wav'
```

**Customization:**
*   **Sounds:** The easiest way to customize is to replace the placeholder `.wav` files in the `sounds/` directory with your own sound files. Ensure they have the same names as listed above. Most common audio formats that `playsound` supports should work (e.g. WAV, MP3).
*   **Key-bindings:** Advanced users can modify the `sound_map` dictionary directly in the `sound_machine.py` script to change which keys trigger which sounds, or to add new sounds and keys.

**Troubleshooting:**
*   **No sound on Linux:** Ensure GStreamer and its plugins are correctly installed as per the "System Dependencies" section.
*   **Permission errors (especially macOS or Linux):** `pynput` might require special permissions to listen to global key events. On Linux, running as root (not generally recommended) or correctly setting up uinput device permissions might be needed for some `pynput` backends. On macOS, you might need to grant accessibility permissions to your terminal application or Python itself.
*   **`pynput` errors in headless environments:** As mentioned in the "Requirements" section, `pynput`'s default backend often requires a display server. You might see errors like "failed to acquire X connection" or "this platform is not supported".

**License:**
*   This project is licensed under the MIT License. See the `LICENSE` file for details.
