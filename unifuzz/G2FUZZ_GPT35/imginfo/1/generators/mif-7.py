import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the 'mif' file with ordered and unordered lists
content = """
# Ordered List
1. Item 1
2. Item 2
3. Item 3

# Unordered List
- Apple
- Banana
- Cherry
"""

# Save the content to a 'mif' file
with open('./tmp/lists.mif', 'w') as file:
    file.write(content)

print("File saved successfully at ./tmp/lists.mif")