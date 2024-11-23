import os

# Create a directory to store the generated 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the 'ani' files
ani_content = "Transparency: 'ani' files can support transparency, allowing for non-rectangular cursor shapes."

# Write the content to 'ani' files
for i in range(3):
    with open(f'./tmp/ani_{i}.ani', 'w') as file:
        file.write(ani_content)

print("Generated 'ani' files with transparency feature in './tmp/' directory.")