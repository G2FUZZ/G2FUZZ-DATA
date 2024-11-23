import os
import random

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_text_sequence(words, repetitions, separator=" "):
    """
    Generate a sequence of repeated words.
    :param words: List of words for each part.
    :param repetitions: List of repetition counts for each word.
    :param separator: Separator used between words.
    :return: Combined string of the sequence.
    """
    sequence = ""
    for word, rep in zip(words, repetitions):
        sequence += (word + separator) * rep
    return sequence.strip()

def add_random_characters(text, intensity=5):
    """
    Add random characters to a text string.
    :param text: String to add characters to.
    :param intensity: Number of random characters to add.
    :return: Modified string with added characters.
    """
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(intensity):
        random_index = random.randint(0, len(text)-1)
        random_char = random.choice(chars)
        text = text[:random_index] + random_char + text[random_index:]
    return text

# Parameters for the text structure
intro_words = ["start", "introduction", "begin"]
verse_words = ["middle", "content", "body"]
outro_words = ["end", "conclusion", "finish"]
word_repetitions = [3, 5, 3]  # Repetitions for each part

# Generate sections
intro_text = generate_text_sequence(intro_words, word_repetitions, separator=", ")
verse_text = generate_text_sequence(verse_words, word_repetitions, separator=", ")
outro_text = generate_text_sequence(outro_words, word_repetitions, separator=", ")

# Combine sections with random characters added
combined_text = add_random_characters(intro_text + ". " + verse_text + ". " + outro_text + ".", intensity=10)

# Define the directory path where the file will be saved
directory_path = './tmp'

# Define the full path for the new file within the specified directory
file_path = os.path.join(directory_path, 'generated_text_with_noise.txt')

# Write the complicated content to the file
try:
    with open(file_path, 'w') as file:
        file.write(combined_text)
    print(f"Complex text file with random characters has been generated at {file_path}")
except IOError as e:
    print(f"An error occurred while writing the text file: {e}")