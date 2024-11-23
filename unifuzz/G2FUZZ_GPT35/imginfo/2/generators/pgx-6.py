import os

# Define the content of the 'pgx' file
content = "Layers: Advanced 'pgx' files may support multiple layers for complex image compositions."

# Create a directory to save the 'pgx' files
os.makedirs("./tmp", exist_ok=True)

# Generate 'pgx' files
for i in range(3):
    filename = f"./tmp/file_{i+1}.pgx"
    with open(filename, "w") as file:
        file.write(content)

print("Generated 'pgx' files successfully.")