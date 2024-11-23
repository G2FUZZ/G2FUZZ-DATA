import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output 'coff' file
output_file_path = os.path.join(output_dir, "example.coff")

# Dummy symbol table entries
symbol_table = [
    {"name": "main", "type": "function", "address": "0x1000"},
    {"name": "helper", "type": "function", "address": "0x1050"},
    {"name": "data", "type": "variable", "address": "0x2000"},
]

# Writing the dummy symbol table to a file
with open(output_file_path, "w") as file:
    file.write("Symbol Table\n")
    file.write("=============\n")
    for symbol in symbol_table:
        file.write(f"Name: {symbol['name']}, Type: {symbol['type']}, Address: {symbol['address']}\n")

print(f"COFF file with dummy symbol table created at: {output_file_path}")