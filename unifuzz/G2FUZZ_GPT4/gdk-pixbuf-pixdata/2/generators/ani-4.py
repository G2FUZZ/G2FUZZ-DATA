def save_ani(frames, durations, filepath):
    """
    Saves frames as an animated GIF, as a stand-in for the .ani format.
    
    :param frames: List of PIL Image objects.
    :param durations: List of frame durations in milliseconds.
    :param filepath: Path to save the animated GIF. Ensure it's directed to ./tmp/.
    """
    # Ensure the directory exists
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    
    # Adjust the filepath to ensure it ends with .gif, and it's saved in ./tmp/
    filepath = os.path.splitext(filepath)[0] + '.gif'
    
    frames[0].save(
        filepath,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        format="GIF",
        transparency=0
    )