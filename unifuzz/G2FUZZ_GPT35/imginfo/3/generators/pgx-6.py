import os

# Create a directory to store the pgx files
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pgx files with metadata
metadata = {
    "sample_information": "Sample ABC",
    "experimental_conditions": "Condition XYZ",
    "research_parameters": {
        "param1": 10,
        "param2": 0.5,
        "param3": "test"
    }
}

for i in range(3):  # Generating 3 pgx files
    filename = f"{directory}file_{i + 1}.pgx"
    with open(filename, 'w') as file:
        file.write("# Metadata\n")
        for key, value in metadata.items():
            if isinstance(value, dict):
                file.write(f"## {key}\n")
                for k, v in value.items():
                    file.write(f"- {k}: {v}\n")
            else:
                file.write(f"- {key}: {value}\n")

print("Generated pgx files with metadata in ./tmp/ directory.")