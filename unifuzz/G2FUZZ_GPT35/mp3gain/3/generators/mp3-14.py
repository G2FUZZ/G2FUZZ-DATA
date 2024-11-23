import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with CBR
with open('./tmp/sample_cbr.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Constant Bit Rate (CBR)')

# Generate and save a sample mp3 file with VBR
with open('./tmp/sample_vbr.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Variable Bit Rate (VBR)')

# Generate and save a sample mp3 file with Gapless playback feature
with open('./tmp/sample_gapless.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Gapless playback feature for seamless track transition')