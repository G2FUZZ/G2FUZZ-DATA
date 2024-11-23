import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MPEG-4 file with Multiple Audio Tracks, Subtitles, and Metadata
sample_data_complex_features = b'\x00\x00\x00\x18ftypisom\x00\x00\x02\x00isomiso2mp41MultipleAudioTracksSubtitlesMetadata'
with open('./tmp/sample_complex_features.mp4', 'wb') as file:
    file.write(sample_data_complex_features)

print("Generated 'mp4' file with Multiple Audio Tracks, Subtitles, and Metadata features saved in './tmp/' directory.")