from app.io.input import input_from_console, input_from_file, input_from_pandas
from app.io.output import output_to_console, output_to_file

def main():
    console_text = input_from_console()
    file_text = input_from_file()
    pandas_text = input_from_pandas()

    output_to_console(console_text)
    output_to_console(file_text)
    output_to_console(pandas_text)

    output_to_file(console_text)
    output_to_file(file_text)
    output_to_file(pandas_text)

if __name__ == "__main__":
    main()
