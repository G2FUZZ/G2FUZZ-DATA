import eyed3
from PIL import Image
from io import BytesIO
import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate dummy mp3 file with multiple ID3 tags, custom frames, and embedded image
with open('./tmp/sample_complex_structure.mp3', 'wb') as f:
    f.write(b'Dummy mp3 content with complex structure')

# Load the generated mp3 file with complex structure
audiofile_complex = eyed3.load('./tmp/sample_complex_structure.mp3')

# Check if audiofile with complex structure is not None before accessing its tag attributes
if audiofile_complex is not None:
    audiofile_complex.tag.artist = 'Complex Artist'
    audiofile_complex.tag.album = 'Complex Album'
    audiofile_complex.tag.title = 'Complex Title'
    audiofile_complex.tag.track_num = 1

    # Add custom frames
    audiofile_complex.tag.frame_set('TXXX', [eyed3.id3.frames.TextFrame('TXXX', description='CustomFrame1', text='Custom frame 1 details')])
    audiofile_complex.tag.frame_set('TXXX', [eyed3.id3.frames.TextFrame('TXXX', description='CustomFrame2', text='Custom frame 2 details')])

    # Embed image into the mp3 file
    image_data = Image.new('RGB', (100, 100), color='red').tobytes()
    image_tag = eyed3.id3.frames.ImageFrame(3, image_data, 'image/jpeg', u'')
    audiofile_complex.tag.images.set(3, image_tag)

    audiofile_complex.tag.save()
    print('Generated mp3 file with complex file structure successfully.')
else:
    print('Error: Failed to load the mp3 file with complex file structure.')