import os
from struct import pack

# Create the ./tmp/ directory if it doesn't already exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Function to create an .ani file with basic sequence control
def create_ani_file(filename):
    # ANI header structure: RIFF, list, info, and anis blocks
    # This example creates a very basic structure for demonstration purposes
    
    # RIFF header
    riff = b'RIFF' + pack('<I', 36) + b'ACON'
    
    # LIST header (listing the animation frames and sequence)
    list_header = b'LIST' + pack('<I', 16) + b'fram'
    
    # INFO (rate and sequence chunks might be included here for a real file)
    # This example does not include a real sequence control for simplicity
    
    # ANI Header (anih)
    # Struct ANIHEADER { DWORD cbSizeOf; DWORD cFrames; DWORD cSteps; DWORD cx, cy; DWORD cBitCount; DWORD cPlanes; DWORD jifRate; DWORD flags; };
    # Assuming a simple ANI with minimal valid data
    anih = b'anih' + pack('<IIIIIIII', 36, 1, 1, 32, 32, 8, 1, 0)  # Example data for a single frame
    
    # Sequence control would be more complex in a real scenario, involving the JIF (jiffies) rate and steps in the ANIHEADER
    # and potentially additional chunks defining the sequence. Here, we keep it simple.
    
    # Assembling the file
    file_content = riff + list_header + anih
    
    # Write the content to an .ani file
    with open(f'./tmp/{filename}.ani', 'wb') as ani_file:
        ani_file.write(file_content)

# Example: Create an example .ani file
create_ani_file('example_animation')