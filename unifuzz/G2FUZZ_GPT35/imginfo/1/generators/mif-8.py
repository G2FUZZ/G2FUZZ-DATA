import os

# Create a directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate the contents of the mif file
mif_content = """
<document>
    <structure>
        <sections>
            <header>
                This is the header section.
            </header>
            <footer>
                This is the footer section.
            </footer>
            <chapters>
                <chapter>
                    Chapter 1: Introduction
                </chapter>
                <chapter>
                    Chapter 2: Methodology
                </chapter>
                <chapter>
                    Chapter 3: Results
                </chapter>
            </chapters>
        </sections>
    </structure>
</document>
"""

# Save the content to a mif file
with open('./tmp/document_structure.mif', 'w') as file:
    file.write(mif_content)

print("mif file generated successfully!")