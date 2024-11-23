import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with subtitles, captions, chapter markers, and closed captioning
for i in range(4):
    with open(f'./tmp/video_{i}.flv', 'wb') as f:
        f.write(b'FLV header')
        f.write(b'Subtitles and captions: This is an example subtitle for video ' + str(i).encode())
        
        # Add chapter markers
        chapter_markers = [b'Chapter 1: Introduction', b'Chapter 2: Main Content', b'Chapter 3: Conclusion']
        for marker in chapter_markers:
            f.write(marker)
        
        # Add closed captioning
        closed_captioning = b'Closed captioning: FLV files can support closed captioning for displaying text-based subtitles synchronized with the video content.'
        f.write(closed_captioning)