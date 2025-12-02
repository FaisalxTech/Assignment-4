filename = "sample.txt"

try:
    # Try to open and read the file
    with open(filename, "r") as f:
        for line in f:
            # Print each line, removing the trailing newline
            print(line.rstrip())
except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"Error: The file '{filename}' was not found.")
