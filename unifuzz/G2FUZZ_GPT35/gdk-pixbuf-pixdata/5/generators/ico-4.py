import zlib

def compress_data(data):
    return zlib.compress(data)

# Generating ICO file with compressed data
icon_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x02\x00\x00\x00\x90b\x02\x92\x00\x00\x00\x03sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00\x0cIDATx\x9c\xed\xc1\t\x00\x00\x00\x05\x00\x01\x00\x02\x00\x85t\x1d\xea\x00\x00\x00\x00IEND\xaeB`\x82'
compressed_icon_data = compress_data(icon_data)

with open('./tmp/compressed_icon.ico', 'wb') as file:
    file.write(compressed_icon_data)

print('ICO file with compression saved successfully.')