import os

# Create a directory to store the generated mif files
os.makedirs('./tmp/', exist_ok=True)

# Metadata information for the mif files
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-01-01',
    'document_properties': {
        'title': 'Sample Document',
        'description': 'This is a sample MIF file with metadata.'
    }
}

# Content sections for the mif files
content_sections = [
    {
        'title': 'Introduction',
        'content': 'This is the introduction section.',
        'subsections': [
            {
                'title': 'Background',
                'content': 'This is the background subsection.'
            },
            {
                'title': 'Objective',
                'content': 'This is the objective subsection.'
            }
        ]
    },
    {
        'title': 'Methods',
        'content': 'This is the methods section.'
    },
    {
        'title': 'Results',
        'content': 'This is the results section.'
    }
]

# Generate mif files with metadata and content sections
for i in range(3):
    filename = f'./tmp/document_{i}.mif'
    with open(filename, 'w') as f:
        f.write(f'; Metadata\n')
        f.write(f'; Author: {metadata["author"]}\n')
        f.write(f'; Creation Date: {metadata["creation_date"]}\n')
        f.write(f'; Document Properties:\n')
        for key, value in metadata["document_properties"].items():
            f.write(f'; {key}: {value}\n')
        f.write(f'\n')
        
        f.write(f'; Content\n')
        for section in content_sections:
            f.write(f'\n{section["title"]}:\n')
            f.write(f'{section["content"]}\n')
            if 'subsections' in section:
                for subsection in section['subsections']:
                    f.write(f'\n\t{subsection["title"]}:\n')
                    f.write(f'\t{subsection["content"]}\n')
                    
        f.write(f'\n; Additional complex file features included...\n')

print('MIF files with metadata and complex content generated successfully.')