import os

def create_ani_file(icon_files, output_file):
    # ANI Header for RIFF format
    RIFF_HEADER = b'RIFF'
    ACON_HEADER = b'ACON'
    LIST_HEADER = b'LIST'
    fram_header = b'fram'
    icon_header = b'icon'
    
    # Calculate the total size of the ani file
    total_size = 4  # For ACON
    chunk_sizes = []
    for icon_file in icon_files:
        if os.path.exists(icon_file):  # Check if the file exists
            with open(icon_file, 'rb') as f:
                content = f.read()
                chunk_sizes.append(len(content))
                total_size += len(content) + 8  # 8 bytes for 'icon' and size fields
        else:
            print(f"Warning: File {icon_file} not found. Skipping.")
            icon_files.remove(icon_file)  # Remove the missing file from the list
    
    total_size += 12  # For LIST and fram headers
    total_size += len(icon_files) * 8  # For each icon header and size
    
    # Create the .ani file
    with open(output_file, 'wb') as f:
        f.write(RIFF_HEADER)
        f.write(total_size.to_bytes(4, byteorder='little'))
        f.write(ACON_HEADER)
        
        # Write the ANI sequence data
        f.write(LIST_HEADER)
        list_chunk_size = total_size - 12  # Subtract RIFF and ACON headers
        f.write(list_chunk_size.to_bytes(4, byteorder='little'))
        f.write(fram_header)
        
        # Write each icon file into the ANI file
        for i, icon_file in enumerate(icon_files):
            if os.path.exists(icon_file):  # Double-check to avoid any potential issues
                f.write(icon_header)
                f.write(chunk_sizes[i].to_bytes(4, byteorder='little'))
                with open(icon_file, 'rb') as icon:
                    f.write(icon.read())

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# List of icon files to include in the ANI file
icon_files = ['./icon1.ico', './icon2.ico']  # Example icon files

# Output ANI file path
output_ani_file = './tmp/animated_cursor.ani'

# Create the ANI file
create_ani_file(icon_files, output_ani_file)