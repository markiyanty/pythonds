def input_from_console():
    """
    Function to input text from the console.
    """
    text = input("Enter text from console: ")
    return text

def input_from_file(file_path="data/input_file.txt"):
    """
    Function to read from a file using Python's built-in capabilities.
    """
    try:
        with open(file_path, "r") as file:
            text = file.read()
        print(text)
        return text
    except FileNotFoundError:
        print("Input file not found.")
        return ""

def input_from_pandas(file_path="data/input_data.csv"):
    """
    Function to read from a file using the pandas library.
    """
    import pandas as pd
    try:
        data_frame = pd.read_csv(file_path)
        text = data_frame.to_string(index=False)
        print(text)
        return text
    except FileNotFoundError:
        print("Input data file not found.")
        return ""
    
input_from_pandas()