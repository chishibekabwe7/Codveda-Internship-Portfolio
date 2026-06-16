# Word Counter
# Codveda Internship - Level 1
# Author: Kabwe Chishibe

import os
import string
from collections import Counter


def display_welcome():
    print("=" * 45)
    print("              WORD COUNTER")
    print("=" * 45)
    print("Reads a text file and analyses its content.\n")


def read_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: '{filepath}'")
    if not os.path.isfile(filepath):
        raise ValueError(f"'{filepath}' is not a file.")
    if not filepath.lower().endswith(".txt"):
        raise ValueError("Only .txt files are supported.")

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def count_words(text):
    return text.split()


def clean_words(words):
    cleaned = []
    for word in words:
        stripped = word.strip(string.punctuation).lower()
        if stripped:
            cleaned.append(stripped)
    return cleaned


def count_sentences(text):
    return sum(text.count(p) for p in ".!?")


def display_results(filepath, raw_words, cleaned_words, text):
    total_words = len(raw_words)
    total_chars = len(text)
    total_chars_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    total_lines = len(text.splitlines())
    total_sentences = count_sentences(text)

    freq = Counter(cleaned_words)
    top_words = freq.most_common(5)

    print(f"\nFile     : {os.path.basename(filepath)}")
    print(f"Path     : {os.path.abspath(filepath)}")
    print("-" * 45)
    print(f"Words            : {total_words}")
    print(f"Lines            : {total_lines}")
    print(f"Sentences (est.) : {total_sentences}")
    print(f"Characters       : {total_chars}")
    print(f"Chars (no spaces): {total_chars_no_spaces}")
    print(f"Unique words     : {len(freq)}")
    print("-" * 45)
    print("Top 5 most frequent words:")
    for rank, (word, count) in enumerate(top_words, 1):
        print(f"  {rank}. '{word}' - {count} time(s)")
    print("=" * 45)


def get_filepath():
    filepath = input("Enter the path to your .txt file: ").strip()
    filepath = filepath.strip("'\"")
    return filepath


def main():
    display_welcome()

    while True:
        filepath = get_filepath()

        try:
            print("\nReading file...")
            text = read_file(filepath)

            if not text.strip():
                print("The file is empty. No words to count.\n")
            else:
                raw_words = count_words(text)
                cleaned_words = clean_words(raw_words)
                display_results(filepath, raw_words, cleaned_words, text)

        except FileNotFoundError as e:
            print(f"\nError: {e}")
            print("Make sure the file path is correct.\n")
        except PermissionError:
            print("\nError: Permission denied. Cannot read this file.\n")
        except UnicodeDecodeError:
            print("\nError: File encoding not supported. Save it as UTF-8.\n")
        except ValueError as e:
            print(f"\nError: {e}\n")

        print()
        again = input("Analyse another file? (yes/no): ").strip().lower()
        print()
        if again not in ("yes", "y"):
            print("Goodbye.")
            print("=" * 45)
            break


if __name__ == "__main__":
    main()