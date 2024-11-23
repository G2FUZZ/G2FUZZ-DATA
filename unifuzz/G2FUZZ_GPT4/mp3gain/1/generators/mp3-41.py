from pydub import AudioSegment
import os
from cryptography.fernet import Fernet

# Improved directory existence check
os.makedirs('./tmp/', exist_ok=True)

# Create a stereo audio segment of silence by combining two mono silent segments
left_silence = AudioSegment.silent(duration=1000)  # 1 second of silence for the left channel
right_silence = AudioSegment.silent(duration=1000)  # 1 second of silence for the right channel
stereo_silence = AudioSegment.from_mono_audiosegments(left_silence, right_silence)

# Export the stereo audio segment as an MP3 file
file_path = "./tmp/stereo_silent_mp3.mp3"
stereo_silence.export(file_path, format="mp3")

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Read the MP3 file data
with open(file_path, 'rb') as file_object:
    file_data = file_object.read()

# Encrypt the file data
encrypted_data = cipher_suite.encrypt(file_data)

# Write the encrypted data back to a new file
encrypted_file_path = "./tmp/encrypted_stereo_silent_mp3.mp3"
with open(encrypted_file_path, 'wb') as encrypted_file_object:
    encrypted_file_object.write(encrypted_data)

print("Stereo MP3 file generated and encrypted without DRM.")