# Generate a 'flv' file with extended features
features = [
    "Editing: FLV files can be edited using various software applications for video production and manipulation.",
    "Scripting Support: FLV files can contain ActionScript code for interactive elements or dynamic behavior within the video.",
    "Multi-Bitrate Streaming: FLV files can be encoded with multiple bitrates to support adaptive bitrate streaming for varying network conditions."
]

file_path = "./tmp/extended_video.flv"

with open(file_path, "w") as file:
    for feature in features:
        file.write(feature + "\n")

print(f"File '{file_path}' with extended features has been generated.")