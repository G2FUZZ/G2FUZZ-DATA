# Generate a 'flv' file with more complex file features
features = [
    "Editing: FLV files can be edited using various software applications for video production and manipulation.",
    "VR (Virtual Reality) Support: FLV files can store VR video content for viewing in virtual reality headsets or environments.",
    "4K Ultra HD Resolution Support: FLV files support playback of videos in 4K Ultra HD resolution for high-quality viewing experience.",
    "Custom Metadata Embedding: FLV files allow embedding custom metadata for additional information and categorization of video content.",
    "Multiple Audio Track Support: FLV files can contain multiple audio tracks for different languages or audio options."
]

file_path = "./tmp/extended_video_with_complex_features.flv"

with open(file_path, "w") as file:
    for feature in features:
        file.write(feature + "\n")

print(f"File '{file_path}' with FLV feature and more complex file features has been generated.")