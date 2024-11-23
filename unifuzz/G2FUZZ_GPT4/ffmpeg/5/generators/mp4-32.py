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
mp4_file = os.path.join(output_dir, "output_with_aac_audio_360_extended.mp4")

# Use FFmpeg to convert the WAV audio to AAC and wrap it in an MP4 container
# Additionally, specify metadata for 360-degree video playback and add Tool Extensions metadata
ffmpeg_cmd = [
    "ffmpeg",
    "-y",  # Overwrite output file if it exists
    "-f", "lavfi",  # Input format to generate a test video pattern
    "-i", "testsrc=size=1920x960:rate=30:duration=" + str(duration),  # Generate a test video pattern in 360 degree resolution
    "-i", wav_file,  # Input audio file
    "-map", "0:v",  # Map video stream
    "-map", "1:a",  # Map audio stream
    "-c:v", "libx264",  # Video codec (H.264)
    "-c:a", "aac",  # Audio codec
    "-b:a", "192k",  # Audio bitrate
    "-metadata:s:v", "stereo_mode=top_bottom",  # Specify stereo mode for 360 video (this example assumes a monoscopic 360 video)
    "-metadata:s:v", "projection_type=equirectangular",  # Specify the projection type (equirectangular for 360 videos)
    "-metadata", "tool_extensions=extended",  # Custom metadata for Tool Extensions feature
    mp4_file
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_cmd)

# Cleanup: Remove the temporary WAV file
os.remove(wav_file)

print(f"MP4 file with AAC audio, 360-degree video, and Tool Extensions feature has been saved to: {mp4_file}")