features = [
    "Editing: FLV files can be edited using various software applications for video production and manipulation.",
    "VR (Virtual Reality) Support: FLV files can store VR video content for viewing in virtual reality headsets or environments."
]

metadata = {
    "title": "Sample FLV Video",
    "author": "John Doe",
    "description": "A sample FLV video with multiple video tracks",
    "date": "2022-01-01"
}

video_tracks = [
    {
        "track_id": 1,
        "resolution": "1920x1080",
        "codec": "H.264"
    },
    {
        "track_id": 2,
        "resolution": "1280x720",
        "codec": "VP9"
    }
]

file_path = "./tmp/complex_video.flv"

with open(file_path, "w") as file:
    file.write("Metadata:\n")
    for key, value in metadata.items():
        file.write(f"{key}: {value}\n")
    file.write("\nFeatures:\n")
    for feature in features:
        file.write(feature + "\n")
    file.write("\nVideo Tracks:\n")
    for track in video_tracks:
        file.write(f"Track ID: {track['track_id']}\n")
        file.write(f"Resolution: {track['resolution']}\n")
        file.write(f"Codec: {track['codec']}\n")
        file.write("\n")

print(f"File '{file_path}' with complex file structures has been generated.")