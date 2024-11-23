import os

# Create a directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate the MIF file with bookmarks
mif_content = """
#MIFFile 4.0
#Bookmarks
<BOOKMARK> FirstChapter
This is the content of the first chapter.
</BOOKMARK>
<BOOKMARK> SecondChapter
This is the content of the second chapter.
</BOOKMARK>
"""

file_path = './tmp/example.mif'

with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file with bookmarks generated at: {file_path}')