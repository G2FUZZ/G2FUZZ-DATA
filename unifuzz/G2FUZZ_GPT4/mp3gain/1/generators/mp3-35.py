from pydub import AudioSegment
from pydub.generators import Sine
import os
from cryptography.fernet import Fernet

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an audio segment of silence
silence = AudioSegment.silent(duration=1000)  # 1 second of silence

# Generate a tone (e.g., 440 Hz for 1 second, which is the A note)
tone_a_generator = Sine(440)
tone_a = tone_a_generator.to_audio_segment(duration=1000)

# Generate another tone (e.g., 523.25 Hz for 1 second, which is the C note)
tone_c_generator = Sine(523.25)
tone_c = tone_c_generator.to_audio_segment(duration=1000)

# Combine these audio segments: silence, A tone, more silence, C tone, and then silence again
combined = silence + tone_a + silence + tone_c + silence

# Export the combined audio segment as an MP3 file
file_path = "./tmp/complex_structure_mp3.mp3"
combined.export(file_path, format="mp3")

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

print("Complex MP3 file generated and encrypted without DRM.")