import os

def create_conditional_texts(conditions, base_text, specific_texts):
    """Generate conditional text blocks for the MIF file."""
    conditional_blocks = [f'<ParaLine\n  <String `{base_text}`>\n> # End ParaLine']
    for condition, text in specific_texts.items():
        conditional_blocks.append(f'<ParaLine\n  <CondText\n    <CTag `{condition}`>\n    <String `{text}`>\n  >\n> # End ParaLine')
    return "\n".join(conditional_blocks)

def create_image_block(image_path, image_caption):
    """Generate an image block for the MIF file."""
    return f'''
<Frame
  <FLocked `No`>
  <FType `Graphic`>
  <ImportObject
    <FDontResize `Yes`>
    <FName `{image_path}`>
  >
>
<PgfTag `Caption`>
<ParaLine
  <String `{image_caption}`>
>
'''

def create_cross_reference(source, target):
    """Generate a cross-reference block for the MIF file."""
    return f'''
<XRef
  <XRefSrcText `{source}`>
  <XRefSrcFile `'>
  <XRefEndText `{target}`>
>
'''

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The path to the MIF file to be created
mif_file_path = './tmp/complex_example.mif'

# Base content for conditional texts
base_text = "General information for all audiences."
specific_texts = {
    "Audience1": "Exclusive insights for Audience 1.",
    "Audience2": "Key takeaways for Audience 2."
}

# Generate conditional text blocks
conditional_content = create_conditional_texts(
    conditions=["Audience1", "Audience2"],
    base_text=base_text,
    specific_texts=specific_texts
)

# Generate an image block
image_block = create_image_block("images/figure1.jpg", "Figure 1: An important diagram.")

# Generate a cross-reference block
cross_reference = create_cross_reference("See Figure 1", "Figure 1: An important diagram.")

# MIF content with more complex file features
mif_content = f"""
<MIFFile 9.00> # Start of the MIF file with version
# Define Conditional Text Settings
<Conditional <CTag `Audience1`> <CState `Show`>>
<Conditional <CTag `Audience2`> <CState `Hide`>>

# Beginning of the content
{conditional_content}

# Image Block
{image_block}

# Cross-reference
{cross_reference}

<Trail MIFFile> # End of the MIF file
"""

# Write the content to the MIF file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'Complex MIF file has been created at {mif_file_path}')