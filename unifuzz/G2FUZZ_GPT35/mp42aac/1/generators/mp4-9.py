import os

# Define the features of the MP4 file
container_format = "MPEG-4 Part 14"
custom_data = "MP4 files can have space to store custom data or user-defined metadata fields."

# Create a directory for saving the generated MP4 files
os.makedirs("./tmp/", exist_ok=True)

# Generate MP4 file with the specified features including Custom data
file_name = "./tmp/generated_file_with_custom_data.mp4"
with open(file_name, "w") as file:
    file.write(f"Container format: {container_format}\nCustom data: {custom_data}")

print(f"MP4 file '{file_name}' with the specified features including Custom data has been generated.")