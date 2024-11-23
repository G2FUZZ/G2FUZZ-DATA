import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

class MP3File:
    def __init__(self, filename):
        self.filename = filename
        self.audio_tracks = []

    def add_audio_track(self, audio_data, track_name):
        self.audio_tracks.append((audio_data, track_name))

    def save_file(self):
        with open(self.filename, 'w') as file:
            file.write('MP3 File:\n')
            for i, (audio_data, track_name) in enumerate(self.audio_tracks):
                file.write(f'Track {i + 1} - {track_name}:\n')
                file.write(audio_data)
                file.write('\n')

# Create an instance of MP3File
filename = './tmp/extended_mp3_file_example.mp3'
mp3_file = MP3File(filename)

# Add audio tracks with different data and track names
mp3_file.add_audio_track('Audio data for track 1', 'Track One')
mp3_file.add_audio_track('Audio data for track 2', 'Track Two')

# Save the MP3 file with multiple audio tracks
mp3_file.save_file()

print(f'Generated mp3 file with multiple audio tracks saved as: {filename}')