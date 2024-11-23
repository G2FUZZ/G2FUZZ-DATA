from pydub import AudioSegment
from pydub.generators import Sine
import os
from cryptography.fernet import Fernet

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple sine wave tones for 2 seconds each, with different frequencies
tones = [Sine(frequency).to_audio_segment(duration=2000) for frequency in [440, 523.25, 587.33]]

# Combine tones into a single track
combined_tone = AudioSegment.silent(duration=0)
for tone in tones:
    combined_tone += tone + AudioSegment.silent(duration=1000)  # Adding silence between tones

# Apply a fade in and fade out to the combined tone
combined_tone = combined_tone.fade_in(200).fade_out(200)

# Adjust volume, making the first half quieter
first_half, second_half = combined_tone[:len(combined_tone)//2], combined_tone[len(combined_tone)//2:]
first_half = first_half - 10  # Decrease volume by 10 dB
combined_tone = first_half + second_half

# Ensure combined_tone is mono before proceeding
combined_tone = combined_tone.set_channels(1)

# Create left and right channels by panning
left_channel = combined_tone.pan(-1)  # Pan fully to the left
right_channel = combined_tone.pan(1)  # Pan fully to the right

# Create a silent stereo track to overlay the left and right channels onto
silent_stereo = AudioSegment.silent(duration=combined_tone.duration_seconds * 1000, frame_rate=combined_tone.frame_rate).set_channels(2)

# Overlay the left and right channels onto the silent stereo track
stereo_tone = silent_stereo.overlay(left_channel).overlay(right_channel, position=0)

# Save the generated tone to a file
file_path = "./tmp/complex_structure_mp3.mp3"
stereo_tone.export(file_path, format="mp3")

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Read the MP3 file data
with open(file_path, 'rb') as file_object:
    file_data = file_object.read()

# Encrypt the file data
encrypted_data = cipher_suite.encrypt(file_data)

# Write the encrypted data back to a new file
encrypted_file_path = "./tmp/encrypted_complex_structure_mp3.mp3"
with open(encrypted_file_path, 'wb') as encrypted_file_object:
    encrypted_file_object.write(encrypted_data)

print("Complex MP3 file with advanced features generated and encrypted without DRM.")