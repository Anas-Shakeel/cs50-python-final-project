import os
import csv
import sys
import json
import random
import re
from time import time
from pyfiglet import Figlet
from tabulate import tabulate
from view_color import display


def main():
    """Color Search Main Application: Entry point"""

    print(intro("CS50P - Final Project", "small"), end="")

    # Loading csv data into memory
    colors_database = read_csv("database.csv")

    """REGEX Patterns"""
    pattern_commands = re.compile(r"^-(.+)", re.IGNORECASE)
    pattern_export = re.compile(
        r"^((?:\w|\s)+) -export -(\w+)$", re.IGNORECASE)
    pattern_view = re.compile(r"^#((?:\w|\d){1,6}) -view$")
    pattern_hex = re.compile(r"^#(\w|\d){1,6}")

    # Printing available commands
    print(show_commands())

    while True:
        try:
            # Getting user input (aka search query)
            query = get_query()

            matches_found = 0
            start_time = time()

            # Commands code here...
            if command_matches := re.match(pattern_commands, query):
                command = command_matches.group(1)

                if command == "list":
                    print(tabulate_it(colors_database))
                    matches_found = len(colors_database)

                elif command == "random":
                    # pick and display a random color from database
                    print(tabulate_it([random.choice(colors_database)]))
                    matches_found = 1

                elif command == "exportall":
                    # Export all colors into a json file
                    export_json("All_Colors.json", colors_database)
                    print(len(colors_database), "Colors Exported")
                    continue

                elif command == "commands":
                    # Show available commands
                    print(show_commands())
                    continue

                else:
                    # Not a Valid Command
                    print("Invalid command!")
                    continue

            # Other functionality
            else:
                # Export Code here...
                if matches := re.match(pattern_export, query):
                    matched_colors = search_query(
                        colors_database, matches.group(1))

                    if not matched_colors:
                        # If matched colors[] is empty
                        print("Nothing to export! Try other keywords")
                        continue

                    if matches.group(2) == "txt":
                        # export to txt
                        data = tabulate_it(
                            matched_colors, format="github")
                        export_txt(f"{matches.group(1)}.txt", data)
                        print(len(matched_colors), "Colors exported")
                        continue

                    elif matches.group(2) == "json":
                        # Export to JSON
                        export_json(f"{matches.group(1)}.json", matched_colors)
                        print(len(matched_colors), "Colors exported")
                        continue

                    else:
                        # for other non-valid attributes
                        print("Invalid command")
                        continue

                # View Commands : searching for pattern_view
                elif matches := re.match(pattern_view, query):
                    color = search_query(colors_database,
                                         matches.group(1), by="Hex")

                    # checking len of colors found
                    if len(color) == 1:
                        print("Showing color...")
                        # execute display
                        display(color_name=color[0]['Name'], color_hex=color[0]['Hex'],
                                color_rgb=f"{color[0]['Red']},{color[0]['Green']},{color[0]['Blue']}")

                    elif len(color) < 1:
                        print("No colors found!")

                    else:
                        print("Need a mode specific hex value")

                    continue

                # Search by Hex Code here...
                elif _ := re.match(pattern_hex, query):
                    matched_hex = search_query(
                        colors_database, query, by="Hex")
                    print(tabulate_it(matched_hex))
                    matches_found = len(matched_hex)

                # Searching Colors by Name
                else:
                    matched_colors = search_query(colors_database, query)
                    print(tabulate_it(matched_colors))
                    matches_found = len(matched_colors)

            end_time = time()-start_time

            
            print(f"{matches_found} Results ({end_time:.2f} seconds)")
            # print(f"Took {end_time:.2f} seconds\n{matches_found} Colors displayed")
            print("+--------------------------+")

        except KeyboardInterrupt:
            sys.exit("Force Exit!")


def intro(intro_text, text_font="slant"):
    """Intro Function, Ascii art stuff"""
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font=text_font)
    return figlet.renderText(intro_text)


def show_commands():
    """A simple function just to print the internal available commands"""
    # Available Commands list
    available_commands = [
        ["-list", "To view all colors"],
        ["-random", "To pick a random color"],
        ["-exportall", "Export all colors into a json file"],
        ["[color] -export [-txt] [-json]","Export color (e.g red -export -txt)"],
        ["[hex value] -view", "Open the color in gui (e.g #343434 -view)"],
        ["-commands", "To display the available commands"],
        ["ctrl+c", "Immediately close the program"],
    ]

    print("Available Commands:")
    return tabulate(available_commands, tablefmt="rounded_grid")


def read_csv(filename):
    """Reads a csv file and returns a list of dictionaries representing every row as a dictionary."""
    if filename and filename.endswith(".csv"):
        try:
            with open(filename) as file:
                reader = csv.DictReader(file)
                return [line for line in reader]
        except FileNotFoundError:
            sys.exit("File not found!")
    else:
        raise TypeError("Not a csv file!")


def get_query():
    """Gets user input for colors as a search query"""
    while True:
        try:
            query = input("\nEnter Query (ctrl+c to exit): ").strip()
            if query:
                return query
            else:
                print("Invalid: Empty Query!")
        except KeyboardInterrupt:
            sys.exit("\nForce Exit!")


def search_query(color_db, query, by='Name'):
    """
    Searches a query (color name) in Colors Database
    and returns a list of matches
    """
    colors_found = []
    for color in color_db:
        if query.lower() in color[by].lower():
            colors_found.append(color)

    return colors_found


def tabulate_it(iterable, format="rounded_grid"):
    """Used to tabulate the displayed data (color details)"""
    return tabulate(iterable, tablefmt=format, headers="keys")


def export_txt(filename, data):
    """Exports the given data into a text file"""

    # if filename is empty or file_extension isn't .txt? raise Error
    if not (filename and filename.endswith(".txt")):
        raise NameError("Not a .txt file")

    # Make a folder to contain all text exported files
    folder = "txt_exports"
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass

    dir = os.path.join(folder, filename)

    # writing data
    with open(dir, "w", encoding="utf-8") as file:
        for item in data:
            file.write(item)

    # Success Message
    print(f"Exported successfully to {dir}")


def export_json(filename, data):
    """Exports the given data into a JSON file"""

    # if filename is empty or file_extension isn't .json? raise Error
    if not (filename and filename.endswith(".json")):
        raise NameError("Not a .json file")

    # Only allow dictionaries to be written in
    if type(data) is str:
        raise TypeError("Data must not be of type: str")

    # Make a folder to contain all text exported files
    folder = "json_exports"
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass

    dir = os.path.join(folder, filename)
    with open(dir, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Exported successfully to {dir}")


if __name__ == "__main__":
    main()
