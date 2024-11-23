import json

# Define resolution settings for the animation
resolution_settings = {
    "width": 1920,
    "height": 1080
}

# Generate the 'ani' file content
ani_content = json.dumps(resolution_settings, indent=4)

# Save the generated 'ani' file into ./tmp/ directory
file_path = './tmp/resolution_settings.ani'
with open(file_path, 'w') as file:
    file.write(ani_content)