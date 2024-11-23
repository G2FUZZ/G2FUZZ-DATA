import os

# Create a directory to store the generated MIF files
os.makedirs('tmp', exist_ok=True)

# Generate MIF file content
mif_content = """
<DOCUMENT>
    <TITLE>Generated MIF File</TITLE>
    <AUTHOR>AI Assistant</AUTHOR>
    <DATE>2022-09-28</DATE>
    <CONTENT>
        This is a sample MIF file generated using Python without any input files.
    </CONTENT>
</DOCUMENT>
"""

# Save the generated MIF file
with open('./tmp/generated_file.mif', 'w') as file:
    file.write(mif_content)

print("MIF file generated successfully.")