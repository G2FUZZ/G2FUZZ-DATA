import os

class MP4File:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tracks = []

    def add_track(self, track_type, track_info):
        self.tracks.append({"type": track_type, "info": track_info})

    def add_metadata(self, metadata):
        with open(self.file_name, "a") as file:
            file.write("\n\nMetadata:\n")
            for key, value in metadata.items():
                file.write(f"{key}: {value}\n")

    def add_chapters(self, chapters):
        with open(self.file_name, "a") as file:
            file.write("\nChapters:\n")
            for chapter_num, title in chapters.items():
                file.write(f"Chapter {chapter_num}: {title}\n")

# Generate a more complex MP4 file
file_name = "./tmp/complex_file.mp4"
mp4_file = MP4File(file_name)

# Add video and audio tracks
mp4_file.add_track("Video", {"resolution": "1920x1080", "codec": "H.264"})
mp4_file.add_track("Audio", {"codec": "AAC", "sampling_rate": "48kHz"})

# Add metadata
metadata = {"Title": "Sample Video", "Author": "John Doe", "Year": "2021"}
mp4_file.add_metadata(metadata)

# Add chapters
chapters = {1: "Introduction", 2: "Main Content", 3: "Conclusion"}
mp4_file.add_chapters(chapters)

print(f"Complex MP4 file '{file_name}' with video, audio tracks, metadata, and chapters has been generated.")