def output_to_console(text):
    """
    Function to output text to the console.
    """
    print("Output to console:")
    print(text)

def output_to_file(text):
    """
    Function to write to a file using Python's built-in capabilities.
    """
    file_path = "data/output.txt"  # Output file path
    with open(file_path, "w") as file:
        file.write(text)
    print("Output written to file:", file_path)
