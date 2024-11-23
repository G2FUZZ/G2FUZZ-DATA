import os

# Create a directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate the MIF file with complex structure
mif_content = """
#MIFFile 4.0
#Bookmarks
<BOOKMARK> Introduction
This is the content of the introduction section.
<BOOKMARK> Chapter1
This is the content of the first chapter.
    <SUBSECTION> Topic1
    This is the content of the first topic in Chapter 1.
    <SUBSECTION> Topic2
    This is the content of the second topic in Chapter 1.
<BOOKMARK> Chapter2
This is the content of the second chapter.
    <SUBSECTION> Topic1
    This is the content of the first topic in Chapter 2.
    <SUBSECTION> Topic2
    This is the content of the second topic in Chapter 2.
"""

file_path = './tmp/complex_example.mif'

with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file with complex file structure generated at: {file_path}')