from moviepy.editor import AudioFileClip, ColorClip
import os
from scipy.io.wavfile import write
import numpy as np

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave
def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * freq * t)
    return (waveform * (2**15 - 1)).astype(np.int16)

# Function to create an FLV file with both video and audio content
def create_flv_with_video(audio_data, sample_rate=44100, codec='mp3', filename='output_with_video.flv', video_duration=5):
    # Generate temporary paths
    temp_audio_path = os.path.join(output_dir, 'temp_audio.wav')
    temp_video_path = os.path.join(output_dir, 'temp_video.mp4')
    temp_mp3_path = os.path.join(output_dir, 'temp_audio.mp3')  # Ensure this is defined outside to be visible for cleanup
    flv_output_path = os.path.join(output_dir, filename)
    
    # Save the audio data to a temporary WAV file
    write(temp_audio_path, sample_rate, audio_data)
    
    # Convert WAV to MP3 (or chosen codec) using moviepy
    audio_clip = AudioFileClip(temp_audio_path)
    audio_clip.write_audiofile(temp_mp3_path, codec=codec, fps=sample_rate)

    # Generate a simple video clip (e.g., a moving rectangle on a solid background)
    color_clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=video_duration)
    color_clip = color_clip.set_fps(24)
    
    # Combine the audio and video clips
    final_clip = color_clip.set_audio(AudioFileClip(temp_mp3_path))
    
    # Write the combined clip to a temporary MP4 file
    final_clip.write_videofile(temp_video_path, codec="libx264", audio_codec=codec)
    
    # Use ffmpeg to convert the MP4 to FLV, ensuring the sample rate is supported
    ffmpeg_command = f"ffmpeg -i {temp_video_path} -ar {sample_rate} -c:v copy -c:a copy {flv_output_path}"
    if os.system(ffmpeg_command) != 0:
        print("Error executing ffmpeg command. Ensure ffmpeg is installed and accessible from the command line.")
    
    # Cleanup temporary files
    os.remove(temp_audio_path)
    os.remove(temp_mp3_path)
    os.remove(temp_video_path)

# Example usage
freq = 440  # Frequency in Hz (A4 note)
duration = 5  # Duration in seconds
sample_rate = 44100  # Example sample rate

waveform = generate_sine_wave(freq, duration, sample_rate=sample_rate)
filename = 'complex_structure_audio_video.flv'
create_flv_with_video(waveform, sample_rate=sample_rate, codec='mp3', filename=filename, video_duration=duration)