def generate_complex_pnm_file(file_name, rows, cols, pixels):
    with open(file_name, 'w') as file:
        file.write("P1\n")
        file.write("# Complex PNM File\n")
        file.write(str(cols) + " " + str(rows) + "\n")
        for row in range(rows):
            for col in range(cols):
                file.write(str(pixels[row][col]) + " ")
            file.write("\n")

file_name = "./tmp/complex_structure.pnm"
rows = 3
cols = 4
pixels = [[0, 1, 0, 1],
          [1, 0, 1, 0],
          [0, 1, 0, 1]]
generate_complex_pnm_file(file_name, rows, cols, pixels)