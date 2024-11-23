import os  # Importing os module to work with the file system

# Function to embed metadata
def embed_metadata(image):
    # PIL expects metadata in this format for PNGs
    meta = PngImagePlugin.PngInfo()

    # Adding text chunks
    meta.add_text("Author", "John Doe")
    meta.add_text("Description", "This is an example of a complex PNG file structure.")
    meta.add_text("Creation Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Embedding the metadata and saving the image in the ./tmp/ directory
    image.save('./tmp/complex_interlaced_image.png', 'PNG', pnginfo=meta, interlace=True)