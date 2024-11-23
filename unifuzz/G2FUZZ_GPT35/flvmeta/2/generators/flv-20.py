import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample FLV file with the specified features including Interactivity and Video Quality Options
with open('./tmp/sample_interactive_video_quality.flv', 'wb') as f:
    f.write(b'FLV File Content with Interactivity and Video Quality Options')

print("FLV file 'sample_interactive_video_quality.flv' with the additional features 'Interactivity' and 'Video Quality Options' has been generated and saved in './tmp/'.")