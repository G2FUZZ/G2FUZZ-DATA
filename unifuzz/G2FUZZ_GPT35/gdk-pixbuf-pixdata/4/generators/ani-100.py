import os

# Create a directory to store the 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Content to be written in the 'ani' file with complex structure
ani_content = """
{
    "file_name": "custom_cursor.ani",
    "author": "John Doe",
    "layers": [
        {
            "name": "layer1",
            "frames": [
                {"image": "frame1.png", "duration": 100},
                {"image": "frame2.png", "duration": 150},
                {"image": "frame3.png", "duration": 200}
            ]
        },
        {
            "name": "layer2",
            "frames": [
                {"image": "frame4.png", "duration": 120},
                {"image": "frame5.png", "duration": 180},
                {"image": "frame6.png", "duration": 220}
            ]
        }
    ]
}
"""

# Write the content to the 'ani' file
with open('./tmp/custom_cursor_complex.ani', 'w') as file:
    file.write(ani_content)

print("'ani' file with complex structure created successfully!")