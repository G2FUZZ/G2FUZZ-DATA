import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample MIF file with bookmarks
mif_content = """
<MIFFile>
    <Title>
        Sample MIF File with Bookmarks
    </Title>
    
    <Content>
        This is a sample MIF file with bookmarks for easier navigation.
        <Bookmark name="chapter1" page="5" />
        <Bookmark name="chapter2" page="10" />
        <Bookmark name="chapter3" page="15" />
    </Content>
</MIFFile>
"""

# Save the generated MIF file
file_path = os.path.join(directory, 'sample.mif')
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f"Generated MIF file saved at: {file_path}")