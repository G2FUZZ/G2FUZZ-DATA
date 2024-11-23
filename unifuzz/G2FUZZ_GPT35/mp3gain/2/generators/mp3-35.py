import eyed3
import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy mp3 file with custom features
with open('./tmp/sample_complex.mp3', 'w') as f:
    f.write('Dummy mp3 content with custom features')

# Load the generated mp3 file with custom features
audiofile = eyed3.load('./tmp/sample_complex.mp3')

# Check if audiofile is not None before accessing its tag attributes
if audiofile is not None:
    audiofile.tag.artist = 'Complex Artist'
    audiofile.tag.album = 'Complex Album'
    audiofile.tag.title = 'Complex Title'
    audiofile.tag.track_num = 1
    audiofile.tag.encoder_settings = 'Complex Encoder Settings'
    
    # Adding custom user-defined text frames
    audiofile.tag.frame_set['CustomFrame1'] = eyed3.id3.frames.TextFrame(b'CustomFrame1', ['Custom data for frame 1'])
    audiofile.tag.frame_set['CustomFrame2'] = eyed3.id3.frames.TextFrame(b'CustomFrame2', ['Custom data for frame 2'])
    
    # Adding image attachment to the mp3 file
    with open('sample_image.jpg', 'rb') as img_file:
        img_data = img_file.read()
        audiofile.tag.images.set(3, img_data, 'image/jpeg', u"Sample image")
    
    audiofile.tag.save()
    print('Generated mp3 file with custom features including custom text frames and image attachment successfully.')
else:
    print('Error: Failed to load the mp3 file.')