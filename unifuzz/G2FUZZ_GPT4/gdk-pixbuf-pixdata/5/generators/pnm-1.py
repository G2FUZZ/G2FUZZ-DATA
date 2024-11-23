# PGM example - a simple grayscale image
pgm_data = "P2\n" + \
           "3 3\n" + \
           "255\n" + \
           "0 128 255\n" + \
           "128 255 0\n" + \
           "255 0 128\n"
with open('./tmp/example.pgm', 'w') as file:
    file.write(pgm_data)  # Corrected variable name here