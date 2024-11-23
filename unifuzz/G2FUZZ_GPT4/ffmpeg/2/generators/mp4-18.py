import numpy as np
from moviepy.editor import AudioFileClip, ColorClip, concatenate_videoclips
import os
from scipy.io.wavfile import write
from cryptography.fernet import Fernet

# Directory to save the generated MP4 file
output_dir = "./tmp/"
output_filename = "aac_audio_example.mp4"

# Generate synthetic audio (1kHz sine wave) for 10 seconds
sample_rate = 44100  # Samples per second
frequency = 1000  # Frequency of the sine wave
duration = 10  # Duration in seconds
t = np.linspace(0, duration, int(sample_rate * duration))
audio = np.sin(2 * np.pi * frequency * t)

# Save the synthetic audio into a temporary WAV file (as an intermediate step)
temp_audio_filename = "temp_audio.wav"
write(temp_audio_filename, sample_rate, audio.astype(np.float32))

# Create an audio clip from the temporary audio file
audio_clip = AudioFileClip(temp_audio_filename)

# Generate a silent video clip of the same duration as the audio
video_clip = ColorClip(size=(640, 480), color=(0, 0, 0), duration=audio_clip.duration)

# Set the audio of the video clip to the generated audio
video_clip = video_clip.set_audio(audio_clip)

# Concatenate the video clip to itself to demonstrate video editing (optional)
final_clip = concatenate_videoclips([video_clip])

# Set the fps for the final clip
final_clip.fps = 24  # Setting fps to 24, but you can choose another value as needed

# Define a function to encrypt data using Fernet (symmetric encryption)
def encrypt_file(input_filepath, output_filepath, key):
    # Initialize Fernet object
    fernet = Fernet(key)
    # Read the original file
    with open(input_filepath, 'rb') as file:
        original = file.read()
    # Encrypt the data
    encrypted = fernet.encrypt(original)
    # Write the encrypted file
    with open(output_filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Generate a key for encryption
key = Fernet.generate_key()

# Specify the path for the encrypted video file
encrypted_output_filename = "encrypted_" + output_filename
encrypted_output_path = f"{output_dir}{encrypted_output_filename}"

# Write the result to a temporary mp4 file before encryption
temp_output_path = f"{output_dir}temp_{output_filename}"
final_clip.write_videofile(temp_output_path, codec="libx264", audio_codec="aac", fps=24)

# Encrypt the video file
encrypt_file(temp_output_path, encrypted_output_path, key)

# Remove the temporary files
os.remove(temp_audio_filename)
os.remove(temp_output_path)

# Display the encryption key to the user (in a real application, store it securely!)
print(f"Encryption key: {key.decode()}")