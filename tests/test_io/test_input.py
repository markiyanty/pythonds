# Test code for input_from_file and input_from_pandas in input.py using pytest

import pytest
import os
from app.io.input import input_from_file, input_from_pandas

# Setup for file existence tests
@pytest.fixture(scope="module")
def setup_file_env():
    # Creating a test text file
    test_text_file = "data/input_file.txt"
    with open(test_text_file, "w") as f:
        f.write("This is a test file.\n")

    # Creating a test CSV file
    test_csv_file = "data/input_data.csv"
    with open(test_csv_file, "w") as f:
        f.write("column1,column2\nvalue1,value2\n")

    yield test_text_file, test_csv_file

def test_input_from_file_exists(setup_file_env):
    test_text_file, _ = setup_file_env
    assert input_from_file() == "This is a test file.\n", "Should read the file content correctly"

def test_input_from_file_not_exists(monkeypatch):
    test_file_path = 'non_existent_file.txt'
    monkeypatch.setattr('app.io.input', lambda x=test_file_path: "")
    assert input_from_file(test_file_path) == "", "Should return an empty string if file does not exist"

def test_input_from_pandas_exists(setup_file_env):
    _, test_csv_file = setup_file_env
    expected_output = "column1 column2\n value1  value2"
    assert input_from_pandas(test_csv_file) == expected_output, "Should correctly read and format CSV content"
    
def test_input_from_pandas_not_exists(monkeypatch):
    non_existent_file_path = 'non_existent_data.csv'
    monkeypatch.setattr('app.io.input', lambda x=non_existent_file_path: "")
    assert input_from_pandas(non_existent_file_path) == "", "Should return an empty string if data file does not exist"

