import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ani' files with looping feature
ani_files = ['animation1.ani', 'animation2.ani', 'animation3.ani']

for file_name in ani_files:
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write("Features: Looping\n")
        file.write("Description: Animations stored in 'ani' files can be set to loop continuously, playing the sequence of frames in a repeating pattern.")

print("Generated 'ani' files with looping feature in './tmp/' directory.")