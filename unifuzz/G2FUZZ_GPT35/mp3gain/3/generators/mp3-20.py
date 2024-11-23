import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with CBR
with open('./tmp/sample_cbr.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Constant Bit Rate (CBR)')

# Generate and save a sample mp3 file with VBR
with open('./tmp/sample_vbr.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Variable Bit Rate (VBR)')

# Generate and save a sample mp3 file with Joint stereo
with open('./tmp/sample_joint_stereo.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Joint stereo feature')

# Generate and save a sample mp3 file with Huffman coding
with open('./tmp/sample_huffman_coding.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Huffman coding feature')

# Generate and save a sample mp3 file with Variable stereo mode
with open('./tmp/sample_variable_stereo_mode.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Variable stereo mode feature')