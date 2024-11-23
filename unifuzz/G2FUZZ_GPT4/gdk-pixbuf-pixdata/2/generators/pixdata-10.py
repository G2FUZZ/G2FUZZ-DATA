import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Since the request involves a concept typically not associated with "pixdata" (vector-based data),
# we'll create an SVG file as an example of resolution-independent vector data.
# SVG is a common vector format that can be scaled without loss of quality.

svg_data = """
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>
"""

# Save the SVG data to a file
with open('./tmp/vector_image.svg', 'w') as file:
    file.write(svg_data)