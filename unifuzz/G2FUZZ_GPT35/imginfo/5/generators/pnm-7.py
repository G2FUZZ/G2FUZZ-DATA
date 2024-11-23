def generate_pnm_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write("P1\n")
        file.write("# " + data + "\n")
        file.write("1 1\n")
        file.write("0\n")

file_name = "./tmp/simple_structure.pnm"
data = "Simple Structure: PNM files have a simple structure, making them easy to read and write programmatically."
generate_pnm_file(file_name, data)