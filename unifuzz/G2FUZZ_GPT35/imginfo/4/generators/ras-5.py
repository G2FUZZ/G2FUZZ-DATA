import os

# Create directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the 'ras' file
content = "5. Platform Independence: The 'ras' format is platform-independent and can be used on different operating systems."

# Save the content to a 'ras' file in the './tmp/' directory
with open('./tmp/file1.ras', 'w') as file:
    file.write(content)

with open('./tmp/file2.ras', 'w') as file:
    file.write(content)

print("Files 'file1.ras' and 'file2.ras' have been generated and saved in the './tmp/' directory.")