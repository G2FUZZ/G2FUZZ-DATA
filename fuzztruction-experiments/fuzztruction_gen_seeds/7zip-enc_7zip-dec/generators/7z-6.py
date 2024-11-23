import py7zr
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# List of compression algorithms to use
compression_algorithms = [
    'LZMA',    # Default, high compression ratio
    'LZMA2',   # Improved version of LZMA
    'PPMd',    # Dmitry Shkarin's PPMdH with small changes
    'BZip2',   # BWT algorithm
    'Deflate', # LZ77-based algorithm, used in zip files
    'Copy',    # No compression
]

# Dummy content to compress
content = {
    "example.txt": b"This is an example content to demonstrate compression algorithms in 7z files."
}

def get_filter_id(algorithm):
    """Map algorithm names to their corresponding py7zr filter IDs."""
    filter_map = {
        'LZMA': py7zr.FILTER_LZMA,
        'LZMA2': py7zr.FILTER_LZMA2,
        'PPMd': py7zr.FILTER_PPMD,
        'BZip2': py7zr.FILTER_BZIP2,
        'Deflate': py7zr.FILTER_DEFLATE,
        'Copy': py7zr.FILTER_COPY,
    }
    return filter_map.get(algorithm, py7zr.FILTER_COPY)  # Default to 'Copy' if not found

for algorithm in compression_algorithms:
    # File name based on the algorithm
    file_name = f'./tmp/example_{algorithm}.7z'
    
    # Compression properties
    filters = [{
        "id": get_filter_id(algorithm)
    }]
    
    with py7zr.SevenZipFile(file_name, 'w', filters=filters) as archive:
        for name, data in content.items():
            # Since we're dealing with bytes, we'll use a workaround to write bytes directly.
            archive.writestr(name, data.decode('utf-8'))  # Decoding bytes to string before writing
    print(f"Created {file_name} using {algorithm} compression algorithm.")