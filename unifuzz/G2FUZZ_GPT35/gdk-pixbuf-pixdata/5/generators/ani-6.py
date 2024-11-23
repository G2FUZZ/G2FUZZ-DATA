import json
import os

# Generate 'ani' file with looping options
ani_data = {
    "loop_continuously": True,  # Set to True for looping continuously, False to play a set number of times
    "loop_times": 3  # Number of times to play the animation if loop_continuously is set to False
}

ani_filename = './tmp/animation.ani'

# Save the generated 'ani' file
with open(ani_filename, 'w') as f:
    json.dump(ani_data, f)

print(f"Generated 'ani' file: {ani_filename}")