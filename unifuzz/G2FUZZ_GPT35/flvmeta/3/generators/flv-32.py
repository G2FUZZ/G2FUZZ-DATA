import os

# Define the content of the FLV file with complex structures
flv_content = """
FLV File Format
- Metadata: FLV files can contain metadata information such as video duration, resolution, and encoding details.
- Cue Points:
    - Cue Point 1: Start Time - 0s, Type - Navigation, Description - Intro
    - Cue Point 2: Start Time - 30s, Type - Event, Description - Main Content Starts
"""

# Create a directory if it doesn't exist
os.makedirs("./tmp", exist_ok=True)

# Save the FLV file with complex file structures
with open("./tmp/complex_file_structures.flv", "w") as file:
    file.write(flv_content)

print("FLV file with complex file structures generated and saved successfully.")