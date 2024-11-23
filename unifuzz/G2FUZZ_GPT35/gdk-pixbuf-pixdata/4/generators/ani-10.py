import os

# Create a directory to store the 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Content to be written in the 'ani' file
ani_content = """10. Editing: Specialized software is available for creating and editing 'ani' files to customize cursor animations."""

# Write the content to the 'ani' file
with open('./tmp/custom_cursor.ani', 'w') as file:
    file.write(ani_content)

print("'ani' file created successfully!")