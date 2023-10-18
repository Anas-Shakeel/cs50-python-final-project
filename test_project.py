import os
from pytest import raises
from project import read_csv
from project import search_query
from project import tabulate_it
from project import export_txt
from project import export_json

csv_path = "test_database.csv"


# read_csv() :>> Accuracy test
def test_read_csv():
    """Tests that 'read_csv' is working correctly.
    that is, reading a csv and returning a list of dicts"""
    # Read 'test_database.csv' for further tests
    data = read_csv(csv_path)

    # Check if any item in the list is even a dictionary
    assert type(data[0]) == dict

    # Check if items in a dict are 'str'
    assert type(data[0]["Name"]) == str

    # Check if it reads all values
    assert len(data[0]) == 6

    # Check if it reads all the values correctly
    assert data[0]["ID"] == "1"
    assert data[0]["Name"] == "Absolute zero"
    assert data[0]["Hex"] == "#0048BA"
    assert data[0]["Red"] == "0"
    assert data[0]["Green"] == "72"
    assert data[0]["Blue"] == "186"

    # Check if it reads all the lines :>> Checklength
    assert len(data) == 9


# read_csv() :>> Errors test
def test_read_csv_errors():
    # Check for 'sys.exit()' if passed invalid file
    with raises(SystemExit):
        read_csv("invalid.csv")

    # Raises 'TypeError' if passed file_extension is not .csv
    with raises(TypeError):
        read_csv("valid.invalidExtention")


# search_query() :>> Accuracy test
def test_search_query():
    """ Check search query. """
    data = read_csv(csv_path)

    results = search_query(data, query="Acid", by="Name")

    # Check results isn't empty
    assert results
    # Check results is a list
    assert type(results) == list
    # Check inside this list is a dictionary/dictionaries
    assert type(results[0]) == dict

    # Check the search is working properly.
    assert results[0]["ID"] == "2"
    assert results[0]["Name"] == "Acid green"
    assert results[0]["Hex"] == "#B0BF1A"


# tabulate_it() :>> Accuracy test
def test_tabulate_it():
    """Not a very robust test but, it is what it is!"""
    # data = read_csv("test_database.csv")
    data = 0

    # Check if passing in an integer throws a 'TypeError'
    with raises(TypeError):
        tabulate_it(data)

    data_2 = ""
    # Check if passing in a string returns a tabulated data, i.e str
    assert type(tabulate_it(data_2)) == str


# export_txt() :>> Accuracy test
def test_export_txt():
    data = read_csv(csv_path)
    # This function expects Type(data) to be str
    export_txt("test.txt", tabulate_it(data))

    # Check if it creates a folder name 'txt_exports'
    assert "txt_exports" in os.listdir()

    # Check if it created a file name 'test.txt' in 'txt_exports' dir
    assert "test.txt" in os.listdir("./txt_exports")


# export_txt() :>> Errors Test
def test_export_txt_errors():
    data = read_csv(csv_path)

    result = tabulate_it(data)

    # Raises 'NameError' if given files other than .txt
    with raises(NameError):
        export_txt("test.bat", result)

    # Raises 'TypeError' if given data other than dicts
    with raises(TypeError):
        export_txt("txt.txt", data)


# export_json() :>> Accuracy test
def test_export_json():
    data = read_csv(csv_path)
    # This Function expects Type(data) to be Dict
    export_json("test.json", data)

    # Check if it creates a folder name 'json_exports'
    assert "json_exports" in os.listdir()

    # Check if it created a file name 'test.json' in 'json_exports' dir
    assert "test.json" in os.listdir("./json_exports")


# export_json() :>> Errors Test
def test_export_json_errors():
    data = read_csv(csv_path)

    results = tabulate_it(data)

    # Raises NameError if file other than .json is passed
    with raises(NameError):
        export_json("test.bat", data)

    # Raises TypeError if data of type 'str' is passed
    with raises(TypeError):
        export_json("json.json", results)
