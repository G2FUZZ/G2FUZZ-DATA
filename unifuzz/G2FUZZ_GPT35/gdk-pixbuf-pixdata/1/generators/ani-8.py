import json

# Create a dictionary representing the features of the 'ani' file
ani_features = {
    "Interactive elements": "'ani' files may support interactive elements within the animation sequence."
}

# Convert the dictionary to JSON format
ani_json = json.dumps(ani_features, indent=4)

# Save the JSON data to a file named 'ani.json' in the './tmp/' directory
with open('./tmp/ani.json', 'w') as file:
    file.write(ani_json)