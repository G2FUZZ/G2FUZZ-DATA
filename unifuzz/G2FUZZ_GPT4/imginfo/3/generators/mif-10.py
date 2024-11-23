import os
import datetime

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
os.makedirs(output_directory, exist_ok=True)

# Metadata details
metadata = {
    'Author': 'Jane Doe',
    'Title': 'Sample Document',
    'CreationDate': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'Keywords': 'MIF, documentation, example'
}

# MIF content with metadata
mif_content = f"""<MIFFile 9.00> # MIF version
<MetaData
 <Author `{metadata['Author']}`>
 <Title `{metadata['Title']}`>
 <CreationDate `{metadata['CreationDate']}`>
 <Keywords `{metadata['Keywords']}`>
> # End of Metadata
"""

# File path
file_path = os.path.join(output_directory, 'sample_metadata.mif')

# Writing the MIF content to a file
with open(file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'MIF file with metadata created at: {file_path}')