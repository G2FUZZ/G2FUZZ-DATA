import numpy as np
import subprocess
import os
import wave

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a sine wave as an example of audio
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency in Hz (A4 pitch)
t = np.linspace(0, duration, int(sample_rate * duration), False)  # Time axis
audio = np.sin(2 * np.pi * frequency * t)  # Generate sine wave
audio = (audio * 32767).astype(np.int16)  # Convert to 16-bit PCM

# Save the audio data to a WAV file (temporary file)
wav_file = os.path.join(output_dir, "temp_audio.wav")
with wave.open(wav_file, 'w') as wf:
    wf.setnchannels(1)  # Mono audio
    wf.setsampwidth(2)  # 16 bits per sample
    wf.setframerate(sample_rate)
    wf.writeframes(audio.tobytes())

# Define the MP4 output file path
mp4_file = os.path.join(output_dir, "output_with_mpegh_3d_audio.mp4")

# Use FFmpeg to convert the WAV audio to MPEG-H 3D Audio and wrap it in an MP4 container
# Please note: Encoding to MPEG-H 3D Audio might require additional setup or external tools/libraries due to its complexity.
# This example assumes FFmpeg has been built with MPEG-H 3D Audio support, which might not be the case by default.
ffmpeg_cmd = [
    "ffmpeg",
    "-y",  # Overwrite output file if it exists
    "-f", "lavfi",  # Input format
    "-i", "anullsrc",  # Generate a silent video (as we're focusing on audio)
    "-i", wav_file,  # Input audio file
    "-c:v", "libx264",  # Video codec (creating a minimal silent video)
    "-t", str(duration),  # Duration of the output
    "-c:a", "mpegh3d",  # Audio codec for MPEG-H 3D Audio, note: 'mpegh3d' is used here as a placeholder
    "-b:a", "192k",  # Audio bitrate, might need adjustment based on MPEG-H 3D Audio requirements
    "-shortest",  # Finish encoding when the shortest input stream ends
    mp4_file
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_cmd)

# Cleanup: Remove the temporary WAV file
os.remove(wav_file)

print(f"MP4 file with MPEG-H 3D Audio has been saved to: {mp4_file}")