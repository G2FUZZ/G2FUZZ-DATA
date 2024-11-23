import eyed3
from PIL import Image
from io import BytesIO
import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy mp3 file with complex structure
with open('./tmp/sample_more_complex_structure.mp3', 'wb') as f:
    f.write(b'Another dummy mp3 content with more complex structure')

# Load the generated mp3 file with more complex structure
audiofile_more_complex = eyed3.load('./tmp/sample_more_complex_structure.mp3')

# Check if audiofile with more complex structure is not None before accessing its tag attributes
if audiofile_more_complex is not None:
    audiofile_more_complex.tag.artist = 'More Complex Artist'
    audiofile_more_complex.tag.album = 'More Complex Album'
    audiofile_more_complex.tag.title = 'More Complex Title'
    audiofile_more_complex.tag.track_num = 1

    # Add multiple custom frames
    audiofile_more_complex.tag.frame_set('TXXX', [
        eyed3.id3.frames.TextFrame('TXXX', description='CustomFrame1', text='Custom frame 1 details'),
        eyed3.id3.frames.TextFrame('TXXX', description='CustomFrame2', text='Custom frame 2 details')
    ])

    # Embed multiple images into the mp3 file
    for i in range(2):
        image_data = Image.new('RGB', (50*(i+1), 50*(i+1)), color='blue').tobytes()
        image_tag = eyed3.id3.frames.ImageFrame(3, image_data, 'image/jpeg', u'Image {}'.format(i+1))
        audiofile_more_complex.tag.images.set(3, image_tag)

    # Add multiple audio frames
    audiofile_more_complex.tag.frame_set('APIC', [
        eyed3.id3.frames.ImageFrame(3, b'Cover Image 1', 'image/jpeg', u'Front Cover'),
        eyed3.id3.frames.ImageFrame(3, b'Cover Image 2', 'image/jpeg', u'Back Cover')
    ])

    audiofile_more_complex.tag.save()
    print('Generated mp3 file with more complex file structure successfully.')
else:
    print('Error: Failed to load the mp3 file with more complex file structure.')