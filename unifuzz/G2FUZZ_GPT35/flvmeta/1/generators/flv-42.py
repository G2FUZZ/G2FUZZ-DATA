import os

def generate_flv_file(output_dir, file_name):
    file_path = os.path.join(output_dir, file_name)
    
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    
    # Video Tag
    video_tag = b'\x09\x00\x00\x00\x02\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00'
    
    # Audio Tag
    audio_tag = b'\x08\x00\x00\x00\x02\x00\x00\x00\x09\x00\x00\x00\x00\x00'
    
    # Metadata Tag
    metadata_tag = b'\x12\x00\x00\x00\x02\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    
    with open(file_path, 'wb') as file:
        file.write(flv_header)
        file.write(video_tag)
        file.write(audio_tag)
        file.write(metadata_tag)
    
    print(f"Complex FLV file generated successfully at: {file_path}")

# Specify the output directory
output_dir = './tmp/'

# Generate a sample FLV file with complex file structures
generate_flv_file(output_dir, 'complex_sample.flv')