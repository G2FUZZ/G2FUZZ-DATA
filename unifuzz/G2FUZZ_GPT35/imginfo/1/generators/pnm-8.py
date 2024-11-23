import os

# Function to generate PNM files
def generate_pnm_files():
    features = "8. Compatibility: PNM files can be easily converted to other image formats using various image processing software."
    filename = "generated_file.pnm"
    directory = "./tmp/"

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, filename), "w") as file:
        file.write(features)

# Generate PNM files
generate_pnm_files()