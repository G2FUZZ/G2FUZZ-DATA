import os

# Function to generate and save PNM files
def generate_pnm_files():
    features = "2. Description: PNM files are a family of image file formats used to store portable bitmap, graymap, and pixmap images."
    
    # Create tmp directory if it doesn't exist
    os.makedirs("./tmp/", exist_ok=True)

    # Generate and save PNM files with the features
    for i in range(3):
        filename = f"./tmp/image_{i}.pnm"
        with open(filename, "w") as file:
            file.write(features)
        print(f"Generated PNM file: {filename}")

# Call the function to generate and save PNM files
generate_pnm_files()