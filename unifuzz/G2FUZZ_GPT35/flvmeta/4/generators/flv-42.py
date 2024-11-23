import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with more complex file structures
for i in range(3):
    with open(f'./tmp/video_{i}.flv', 'wb') as f:
        # FLV header
        f.write(b'FLV header')

        # Video metadata
        video_metadata = b'Video Metadata: { "title": b"Video ' + str(i).encode() + b'", "duration": b"5 mins" }'
        f.write(video_metadata)

        # Audio tracks
        for audio_track in range(2):  # Generate 2 audio tracks
            audio_data = b'Audio Track ' + str(audio_track).encode() + b': Audio Data...'
            f.write(audio_data)

        # Subtitles
        subtitles = [
            b'Subtitles: English - This is an example English subtitle for video ' + str(i).encode(),
            b'Subtitles: Spanish - Esto es un ejemplo de subt\xc3\xadtulo en espa\xc3\xb1ol para el video ' + str(i).encode()
        ]
        for subtitle in subtitles:
            f.write(subtitle)