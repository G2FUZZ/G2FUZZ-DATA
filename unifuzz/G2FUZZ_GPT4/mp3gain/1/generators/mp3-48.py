import os
import numpy as np
from pydub import AudioSegment
from cryptography.fernet import Fernet

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create different audio segments of silence with effects
silence_sine = AudioSegment.silent(duration=1000)  # 1 second of silence
silence_square = AudioSegment.silent(duration=1000)  # 1 second of silence
silence_sawtooth = AudioSegment.silent(duration=1000)  # 1 second of silence

# Apply a fade-in effect to each silent segment
fade_duration = 2000  # 2 seconds, but capped by the duration of the silence itself
silence_sine = silence_sine.fade_in(fade_duration)
silence_square = silence_square.fade_in(fade_duration)
silence_sawtooth = silence_sawtooth.fade_in(fade_duration)

# Combine the silent segments into a single track
combined_silence = silence_sine + silence_square + silence_sawtooth

# Export the combined silent segments as an mp3
combined_silence.export('./tmp/complex_silent.mp3', format='mp3')

# Generate a sequence of silent segments to create a more complex silence pattern
durations = np.linspace(1000, 500, 5)  # Example: from 1000 ms to 500 ms
complex_silence = None
for duration in durations:
    temp_silence = AudioSegment.silent(duration=int(duration)).fade_in(200)
    complex_silence = temp_silence if complex_silence is None else complex_silence + temp_silence

# Export the complex silence pattern as an mp3
complex_silence.export('./tmp/complex_silence_pattern.mp3', format='mp3')

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt and write the complex silent segments back to new files
for file_name in ['complex_silent.mp3', 'complex_silence_pattern.mp3']:
    file_path = f"./tmp/{file_name}"
    # Read the MP3 file data
    with open(file_path, 'rb') as file_object:
        file_data = file_object.read()

    # Encrypt the file data
    encrypted_data = cipher_suite.encrypt(file_data)

    # Write the encrypted data back to a new file
    encrypted_file_path = f"./tmp/encrypted_{file_name}"
    with open(encrypted_file_path, 'wb') as encrypted_file_object:
        encrypted_file_object.write(encrypted_data)

print("Complex silent MP3 files generated and encrypted without DRM.")