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
mp4_file = os.path.join(output_dir, "output_with_aac_audio.mp4")

# Use FFmpeg to convert the WAV audio to AAC and wrap it in an MP4 container
ffmpeg_cmd = [
    "ffmpeg",
    "-y",  # Overwrite output file if it exists
    "-f", "lavfi",  # Input format
    "-i", "anullsrc",  # Generate a silent video (as we're focusing on audio)
    "-i", wav_file,  # Input audio file
    "-c:v", "libx264",  # Video codec (creating a minimal silent video)
    "-t", str(duration),  # Duration of the output
    "-c:a", "aac",  # Audio codec
    "-b:a", "192k",  # Audio bitrate
    "-shortest",  # Finish encoding when the shortest input stream ends
    mp4_file
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_cmd)

# Cleanup: Remove the temporary WAV file
os.remove(wav_file)

# To create content for adaptive streaming (like MPEG-DASH),
# we need to split the original MP4 into multiple bitrates and segments.
dash_dir = os.path.join(output_dir, "dash")
os.makedirs(dash_dir, exist_ok=True)

ffmpeg_dash_cmd = [
    "ffmpeg",
    "-y",  # Overwrite output files if they exist
    "-i", mp4_file,  # Input file
    "-map", "0",  # Use all streams from the input file
    "-c:v", "libx264",  # Video codec for transcoding
    "-c:a", "aac",  # Audio codec
    "-b:v:0", "500k",  # First video bitrate variant
    "-b:v:1", "1000k",  # Second video bitrate variant
    "-b:a:0", "128k",  # Audio bitrate
    "-s:v:0", "640x360",  # First video resolution variant
    "-s:v:1", "1280x720",  # Second video resolution variant
    "-use_timeline", "1",  # MPEG-DASH specific options
    "-use_template", "1",  # MPEG-DASH specific options
    "-adaptation_sets", "id=0,streams=v id=1,streams=a",  # Define adaptation sets
    "-f", "dash",  # Format for output
    os.path.join(dash_dir, "output.mpd")  # Output DASH Manifest file
]

# Execute the FFmpeg command to create DASH content
subprocess.run(ffmpeg_dash_cmd)

print(f"MP4 file with AAC audio has been saved to: {mp4_file}")
print(f"Adaptive streaming content has been generated at: {dash_dir}")