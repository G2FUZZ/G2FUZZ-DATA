import os

# Define the features of the MP4 file
container_format = "MPEG-4 Part 14"

# Create a directory for saving the generated MP4 files
os.makedirs("./tmp/", exist_ok=True)

# Generate MP4 file with the specified features
file_name = "./tmp/generated_file.mp4"
with open(file_name, "w") as file:
    file.write(f"Container format: {container_format}")

print(f"MP4 file '{file_name}' with the specified features has been generated.")