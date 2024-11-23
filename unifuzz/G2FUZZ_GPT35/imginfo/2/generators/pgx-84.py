import os
import random

# Define the file header for pgx files
file_header = "PGX FILE FORMAT\n"

# Function to generate random metadata
def generate_metadata():
    metadata = f"Metadata:\n"
    metadata += f"Date: {random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(2000, 2022)}\n"
    metadata += f"Author: {random.choice(['Alice', 'Bob', 'Charlie', 'David'])}\n"
    return metadata

# Function to generate random nodes information
def generate_nodes(num_nodes):
    nodes_info = "Nodes:\n"
    for i in range(num_nodes):
        node_id = i + 1
        node_data = f"Node {node_id}: {random.choice(['A', 'B', 'C', 'D'])}\n"
        nodes_info += node_data
    return nodes_info

# Function to generate random edges information
def generate_edges(num_edges, num_nodes):
    edges_info = "Edges:\n"
    for i in range(num_edges):
        source = random.randint(1, num_nodes)
        target = random.randint(1, num_nodes)
        edge_data = f"Edge {i + 1}: {source} --> {target}\n"
        edges_info += edge_data
    return edges_info

# Create a directory to store the pgx files if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate pgx files with the specified features
num_files = 5
num_nodes = 10
num_edges = 15

for i in range(num_files):
    filename = f'{output_dir}file_{i+1}.pgx'
    with open(filename, 'w') as file:
        file.write(file_header)
        file.write(generate_metadata())
        file.write(generate_nodes(num_nodes))
        file.write(generate_edges(num_edges, num_nodes))

print(f'{num_files} pgx files generated and saved in {output_dir}')