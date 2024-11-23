import os

# Create a directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate the content for the 'ani' file
ani_content = """
{
    "looping": true
}
"""

# Save the generated content to a file
output_file = os.path.join(output_dir, 'generated.ani')
with open(output_file, 'w') as file:
    file.write(ani_content)

print(f"Generated 'ani' file saved at: {output_file}")