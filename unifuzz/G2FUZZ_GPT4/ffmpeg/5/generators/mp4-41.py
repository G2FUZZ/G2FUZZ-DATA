import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.editor import clips_array, VideoFileClip, AudioFileClip, concatenate_videoclips
from scipy.io.wavfile import write as write_wav

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define parameters for the animation
frames = 100  # Number of frames in the animation
fps = 10  # Frames per second

def create_complex_animation(angle_functions, file_path, with_sound=False):
    fig, axs = plt.subplots(nrows=1, ncols=len(angle_functions), figsize=(5 * len(angle_functions), 5))
    if len(angle_functions) == 1:  # Ensure axs is iterable
        axs = [axs]
    lines = [ax.plot([], [], 'r-')[0] for ax in axs]

    for ax in axs:
        ax.set_xlim(0, 2*np.pi)
        ax.set_ylim(-1, 1)

    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def update(frame):
        for i, angle_function in enumerate(angle_functions):
            xdata = frame * 2 * np.pi / frames
            ydata = angle_function(xdata)
            lines[i].set_data(np.append(lines[i].get_xdata(), xdata), np.append(lines[i].get_ydata(), ydata))
        return lines

    ani = FuncAnimation(fig, update, frames=range(frames),
                        init_func=init, blit=True)
    ani.save(file_path, writer='ffmpeg', fps=fps)
    plt.close(fig)

    if with_sound:
        # Generate a simple sine wave as a placeholder sound
        sample_rate = 44100
        t = np.linspace(0, frames / fps, frames * sample_rate // fps, endpoint=False)
        sine_wave = np.sin(2 * np.pi * 220 * t).astype(np.float32)  # 220 Hz sine wave
        audio_file_path = os.path.join(output_dir, "sound.wav")
        write_wav(audio_file_path, sample_rate, sine_wave)

        # Add the audio to the video clip
        video_clip = VideoFileClip(file_path)
        audio_clip = AudioFileClip(audio_file_path)
        video_clip_with_audio = video_clip.set_audio(audio_clip)
        final_file_path = os.path.splitext(file_path)[0] + "_with_sound.mp4"
        video_clip_with_audio.write_videofile(final_file_path, fps=fps)

        # Cleanup
        video_clip.close()
        audio_clip.close()
        os.remove(audio_file_path)  # Remove the temporary audio file
        print(f"Generated video with sound at: {final_file_path}")
    else:
        print(f"Generated video at: {file_path}")

# Define different "angle" functions
def angle1(x):
    return np.sin(x)

def angle2(x):
    return np.cos(x)

def angle3(x):
    return np.sin(2*x)

def angle4(x):
    return np.cos(2*x)

# Create a complex animation with subplots and sound
file_path = os.path.join(output_dir, "complex_animation.mp4")
create_complex_animation([angle1, angle2, angle3, angle4], file_path, with_sound=True)