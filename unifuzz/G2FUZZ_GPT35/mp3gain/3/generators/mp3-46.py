import os
import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import soundfile as sf

# Create a stereo WAV file with DRM, MPEG audio version, and Crossfade support features
stereo_sound_drm_mpeg_crossfade = Sine(440).to_audio_segment(duration=1000)
# Add DRM feature (in this case, we will just add a comment to indicate DRM protection)
drm_comment = "DRM Protection: Unauthorized copying or distribution is prohibited."
stereo_sound_drm_mpeg_crossfade += AudioSegment.silent(duration=len(drm_comment)*1000)
# Add MPEG audio version feature
mpeg_version_comment = "MPEG Audio Version: MPEG-1"
stereo_sound_drm_mpeg_crossfade += AudioSegment.silent(duration=len(mpeg_version_comment)*1000)
# Add Crossfade support feature
crossfade_comment = "Crossfade support: Smooth transitions between tracks by overlapping audio."
stereo_sound_drm_mpeg_crossfade += AudioSegment.silent(duration=len(crossfade_comment)*1000)

# Convert stereo audio to a numpy array
audio_data = stereo_sound_drm_mpeg_crossfade.get_array_of_samples()
sample_width = stereo_sound_drm_mpeg_crossfade.sample_width
channels = stereo_sound_drm_mpeg_crossfade.channels

# Split stereo audio into left and right channels
if channels == 2:
    audio_data_left = audio_data[::channels]
    audio_data_right = audio_data[1::channels]
else:
    # For mono audio, duplicate the audio data for both left and right channels
    audio_data_left = audio_data
    audio_data_right = audio_data

sample_rate = stereo_sound_drm_mpeg_crossfade.frame_rate

# Combine stereo audio channels
audio_data_stereo = np.column_stack((audio_data_left, audio_data_right))

# Save the stereo audio data as a WAV file
file_path = "./tmp/stereo_sound_drm_mpeg_crossfade.wav"
sf.write(file_path, audio_data_stereo, sample_rate)

# Add metadata to the WAV file
audio_segment = AudioSegment.from_file(file_path, format="wav")
audio_segment.export(file_path, format="mp3", tags={"drm": "Unauthorized copying or distribution is prohibited.", "mpeg_version": "MPEG-1", "crossfade_support": "Smooth transitions between tracks by overlapping audio."})

print(f"Stereo WAV file with DRM, MPEG audio version, and Crossfade support features saved at: {file_path}")