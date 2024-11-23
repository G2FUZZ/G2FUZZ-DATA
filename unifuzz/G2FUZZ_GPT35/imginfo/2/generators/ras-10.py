import os

# Define the feature content
feature_content = "10. Applications: Compatible with various image viewing and editing software."

# Create a directory to store the files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the 'ras' file
with open('./tmp/feature.ras', 'w') as file:
    file.write(feature_content)

print("Feature file 'feature.ras' has been generated and saved in the './tmp/' directory.")