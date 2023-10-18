# THE COLORS PROJECT

#### [Video Demo](https://www.youtube.com/watch?v=X-JD-oCxOzU&t=11s)


## Description:

`@thecolorsproject` is a program that allows users to search colors either by their name or hex value and get all colors that matched the entered query. It uses multiple __regex patterns__ to dynamically detect the user's query and perform operations accordingly. There are different built-in commands that user can use for different purposes like `-list` command used to display all the available colors in database and more.

__There are more of these built-in commands. each with their own functionality. all of them are explained in `HOW TO USE` section.__

### Features
- Search by __name__ or __hex__ value
- Pick a random color
- View color in a GUI window
- User Friendly Output
- Easy to use
- Built-in commands
- Contains upto __1754__ colors
- Export data into `json` or `text` files
- Displays the time it took to search
- Displays the number of results found

## Usage
1. Install [Python 3.11.2](https://www.python.org/download)
2. Open up terminal or command prompt and make sure you are in the same directory as project. e.g `C:\Users\Admin\Downloads\project>`
3. Install the required dependencies using pip: `pip install -r requirements.txt`
4. Run the program simply by double-clicking `project.py` in file explorer (__recommended__) or by executing `python project.py` in the terminal or command prompt 

## HOW TO USE
> After opening the program, you will see a heading (in ascii) and a table containing a list of commands and their functions like the following
> ```
>   ___ ___ ___  __  ___         ___ _           _   ___          _        _
>  / __/ __| __|/  \| _ \  ___  | __(_)_ _  __ _| | | _ \_ _ ___ (_)___ __| |_
> | (__\__ \__ \ () |  _/ |___| | _|| | ' \/ _` | | |  _/ '_/ _ \| / -_) _|  _|
>  \___|___/___/\__/|_|         |_| |_|_||_\__,_|_| |_| |_| \___// \___\__|\__|
>                                                              |__/
> Available Commands:
> ╭────────────────────────────────┬───────────────────────────────────────────╮
> │ -list                          │ To view all colors                        │
> ├────────────────────────────────┼───────────────────────────────────────────┤
> │ -random                        │ To pick a random color                    │
> ├────────────────────────────────┼───────────────────────────────────────────┤
> │ -exportall                     │ Export all colors into a json file        │
> ├────────────────────────────────┼───────────────────────────────────────────┤
> │ [color] -export [-txt] [-json] │ Export search (e.g red -export -txt)      │
> ├────────────────────────────────┼───────────────────────────────────────────┤
> │ [hex value] -view              │ Open the color in gui (e.g #343434 -view) │
> ├────────────────────────────────┼───────────────────────────────────────────┤
> │ -commands                      │ To display the available commands         │
> ├────────────────────────────────┼───────────────────────────────────────────┤
> │ ctrl+c                         │ Immediately close the program             │
> ╰────────────────────────────────┴───────────────────────────────────────────╯
> 
> Enter Query (ctrl+c to exit):
> ```
> In the `Enter Query (ctrl+c to exit):` you can type any valid command or search for any color
>
> ### Searching colors
> There are two methods to search colors
> > 1. by name (e.g Type `Silver` and hit __enter__)
> > ```
> > Enter Query (ctrl+c to exit): Silver
> > ╭──────┬──────────────────┬─────────┬───────┬─────────┬────────╮
> > │   ID │ Name             │ Hex     │   Red │   Green │   Blue │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1194 │ Pale silver      │ #C9C0BB │   201 │     192 │    187 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1344 │ Quick Silver     │ #A6A6A6 │   166 │     166 │    166 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1397 │ Roman silver     │ #838996 │   131 │     137 │    150 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1486 │ Silver           │ #C0C0C0 │   192 │     192 │    192 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1487 │ Silver Lake blue │ #5D89BA │    93 │     137 │    186 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1488 │ Silver chalice   │ #ACACAC │   172 │     172 │    172 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1489 │ Silver pink      │ #C4AEAD │   196 │     174 │    173 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1490 │ Silver sand      │ #BFC1C2 │   191 │     193 │    194 │
> > ├──────┼──────────────────┼─────────┼───────┼─────────┼────────┤
> > │ 1518 │ Sonic silver     │ #757575 │   117 │     117 │    117 │
> > ╰──────┴──────────────────┴─────────┴───────┴─────────┴────────╯
> > 9 Results (0.02 seconds)
> > +--------------------------+
> > ```
> > After hitting enter, you will see all the colors which have `Silver` in their name
> > 
> > It also shows __time it took__ to complete the search and the __number of results__ found.
>
> > 2. by hex value (e.g Type `#C0C0C0` and hit enter)
> > ```
> > Enter Query (ctrl+c to exit): #C0C0C0
> > ╭──────┬────────┬─────────┬───────┬─────────┬────────╮
> > │   ID │ Name   │ Hex     │   Red │   Green │   Blue │
> > ├──────┼────────┼─────────┼───────┼─────────┼────────┤
> > │ 1486 │ Silver │ #C0C0C0 │   192 │     192 │    192 │
> > ╰──────┴────────┴─────────┴───────┴─────────┴────────╯
> > 1 Results (0.00 seconds)
> > +--------------------------+
> > ```
> > After hitting enter you will see all the colors that have `#C0C0C0` in their hex value.
> 
> ### Built-in commands
> There are some __Built-in commands__ available to use for different purposes.
> > - `-list` will display a list of all colors. Type `-list` and hit enter.
> > ```
> > Enter Query (ctrl+c to exit): -list
> >╭──────┬──────────────────────┬─────────┬───────┬─────────┬────────╮
> >│   ID │ Name                 │ Hex     │   Red │   Green │   Blue │
> >├──────┼──────────────────────┼─────────┼───────┼─────────┼────────┤
> >│    1 │ Absolute zero        │ #0048BA │     0 │      72 │    186 │
> >├──────┼──────────────────────┼─────────┼───────┼─────────┼────────┤
> >│    2 │ Acid green           │ #B0BF1A │   176 │     191 │     26 │
> >├──────┼──────────────────────┼─────────┼───────┼─────────┼────────┤
> >│  ... │ ........             │ ....... │   ... │     ... │     .. │
> >├──────┼──────────────────────┼─────────┼───────┼─────────┼────────┤
> >│ 1754 │ Zomp                 │ #39A78E │    57 │     167 │    142 │
> >╰──────┴──────────────────────┴─────────┴───────┴─────────┴────────╯
> > 1754 Results (0.28 seconds)
> > +--------------------------+
> > ```
>
> > - `-random` will pick and display any random color from database. Type `-random` and hit enter.
> >```
> >Enter Query (ctrl+c to exit): -random
> >╭──────┬────────┬─────────┬───────┬─────────┬────────╮
> >│   ID │ Name   │ Hex     │   Red │   Green │   Blue │
> >├──────┼────────┼─────────┼───────┼─────────┼────────┤
> >│  165 │ Brass  │ #B5A642 │   181 │     166 │     66 │
> >╰──────┴────────┴─────────┴───────┴─────────┴────────╯
> > 1 Results (0.00 seconds)
> > +--------------------------+
> >```
>
> > - `-exportall` will export all colors in __.\json_exports\All_Colors.json__. Type `-exportall` and hit enter
> > ```
> > Enter Query (ctrl+c to exit): -exportall
> > Exported successfully to json_exports\All_Colors.json
> > 1754 Colors Exported
> > ```
>
> > - `[color] -export -[txt][json]` wil export all colors which have the name in their name into a json or text file. <br>
> > Type `black -export -[txt][json]` and hit enter.
> > ```
> > Enter Query (ctrl+c to exit): black -export -txt
> > Exported successfully to txt_exports\black.txt
> > 15 Colors exported
> > 
> > Enter Query (ctrl+c to exit): black -export -json
> > Exported successfully to json_exports\black.json
> > 15 Colors exported
> > ```
>
> > - `[hex value] -view` will open up a window showing the color. Type `#B76E79 -view` and hit enter.
> > ```
> > Enter Query (ctrl+c to exit): #B76E79 -view
> > Showing color...
> > ```
>
> > - `-commands` will show all available commands. Type `-commands` and hit enter.
> > ```
> > Enter Query (ctrl+c to exit): -commands
> > Available Commands:
> > ╭────────────────────────┬───────────────────────────────────────────╮
> > │ -list                  │ To view all colors                        │
> > ├────────────────────────┼───────────────────────────────────────────┤
> > │ -random                │ To pick a random color                    │
> > ├────────────────────────┼───────────────────────────────────────────┤
> > │ -exportall             │ Export all colors into a json file        │
> > ├────────────────────────┼───────────────────────────────────────────┤
> > │ -export [-txt] [-json] │ Export search (e.g red -export -txt)      │
> > ├────────────────────────┼───────────────────────────────────────────┤
> > │ -view                  │ Open the color in gui (e.g #343434 -view) │
> > ├────────────────────────┼───────────────────────────────────────────┤
> > │ -commands              │ To display the available commands         │
> > ├────────────────────────┼───────────────────────────────────────────┤
> > │ ctrl+c                 │ Immediately close the program             │
> > ╰────────────────────────┴───────────────────────────────────────────╯
> > ```
>
> > - `ctrl+c` will close the whole program Immediately.
> > ```
> > Enter Query (ctrl+c to exit): 
> > Force Exit!
> > ```
>

---

## Libraries used in this project
> ### Built-in
> >`os` <br>
> > it was used to create folders and filenames using __os.path.join()__ and __os.mkdir()__ functions.
> >
> > `csv` <br>
> > it was used to read '__database.csv__' file using __csv.DictWriter()__ function.
> >
> > `sys` <br>
> > it was used to close the program upon __KeyboardInterruptions__ using __sys.exit()__ function.
> >
> > `json` <br>
> > it was used to write data into json files using __json.dump()__ function.
> >
> > `random` <br>
> > it was used to pick a random color from 'colors_database' for __-random__ command using __random.choice()__ function.
> >
> > `re` <br>
> > it was used to search for specific patterns in user input to distinguish between commands, color names & hex values using __re.compile()__ to compile different regex patterns and __re.match()__ to match for these patterns.<br>
> > Further __match.group()__ was used to extract groups from these matches.
> >
> > `time` <br>
> > it was used to show the seconds it took to complete the search by subtracting __start_time__ from __current_time__ using __time()__ function.
> >
> > `pytest` <br>
> > it was used in __test_project.py__ to check for errors using __raises()__ function.
>
>
> ### External
> > `pyfiglet` <br>
> > it was used to display the '__CS50P-Final Project__' in ascii art using __Figlet__ class.
> >
> > `tabulate` <br>
> > it was used to display the tabular data using __tabulate()__ function.
> >
> > `tkinter` <br>
> > it was used by '__view_color.py__' file to display colors in graphical user interface GUI.
> >
> > `pyperclip` <br>
> > it was also used by '__view_color.py__' to allow users to copy rgb and hex values with a click of a button. __pyperclip.copy()__ function was used for this purpose.
>

---

## Project's root directory
- `project.py`
- `test_project.py`
- `view_color.py`
- `database.csv`
- `test_database.csv`
- `README.md`
- `requirements.txt` 
- `python_icon.ico`


## Overview of `project.py`
This is the main file of the project. this file contains 9 functions including `main`

> ### Functions
>
> - `main` <br>
> This is the entry point of the program and handles the flow of program. It contains a whole lot of __conditional statements__ to make the program as dynamic as possible. It also executes other functions within this file and __view_color__ file.
>
> - `intro(into_text, text_font)` <br> 
> This function takes two parameters __intro_text__ (the text to be displayed) and __text_font__ (the font to apply) and returns a string in Ascii art using __pyfiglet__ module. Which then gets printed from within the __main__ function. CS50 heading at the start of program was printed using this function.
>
> - `show_commands` <br>
> It returns the built-in commands in a tabular form using __tabulate__ module. Which gets printed in the main function. It has a list of lists of commands and their functionality like shown below.
> > ``` python
> > available_commands = [
> >         ["-list", "To view all colors"],
> >         ["-random", "To pick a random color"],
> >         ["-exportall", "Export all colors into a json file"],
> >         ["[color] -export [-txt] [-json]","Export color (e.g red -export -txt)"],
> >         ["[hex value] -view", "Open the color in gui (e.g #343434 -view)"],
> >         ["-commands", "To display the available commands"],
> >         ["ctrl+c", "Immediately close the program"],
> >     ]
> > ```
>
> - `read_csv(filename)` <br>
> This function takes one parameter __filename__ and then reads file using __DictReader__ from __csv__ module and returns a list of dictionaries.
>
> - `get_query` <br>
> This function takes user input and returns the query. If the query is empty, it prompts the user again until user entered something. Further checking and pattern matching happens in the __main__ function.
>
> - `search_query(color_db, query, by='Name')` <br>
> This function searches a query (colorname or hexcode) in the colors database and returns all the matching results. Which then gets tabulted and printed from within the __main__ function.<br>
> This function takes three parameters. 
>   - __color_db__: for the database to search-in.
>   - __query__: for the query to search.
>   - __by__: where to search (in names or hex values).
>
> - `tabulate_it(iterable, format="rounded_grid")` <br>
> This function takes an __iterable__ and returns a string containing the iterable's values in tabulated form. It uses __tabulate__ module for this. Which gets printed in the __main__ function. <br>
> This function takes two parameters.
>   - __iterable__: values to put in the table
>   - __format__: the format to apply to the table
>
> - `export_txt(filename, data)` <br>
> This function __file.write()__ to exports the given data in __.\txt_exports\filename.txt__. <br>
> This function takes two parameters.
>   - __filename__: the file to create/overwrite
>   - __data__: the data to write
>
> - `export_json(filename, data)` <br>
> This function uses __json.dump()__ from `json` module to exports the given data in __.\json_exports\filename.json__. <br>
> This function takes two parameters.
>   - __filename__: the file to create/overwrite
>   - __data__: the data to write
>


## Overview of `test_project.py`
This function tests the functionality of `project.py` using a unit testing framework called __pytest__. this file has a total of 8 functions which test the functions from `project.py` thoroughly.

> ### Functions
> `test_read_csv` <br>
> This function tests the functionality of __read_csv__ function from __project.py__ and checks whether or not the function is returning correct values in correct order.
>
> `test_read_csv_errors` <br>
> This function tests the functionality of __read_csv__ function from __project.py__ and checks whether or not it is raising errors upon pasing invalid or non-existing file.
>
> `test_search_query` <br>
> This function tests __search_query__ from __project.py__ and checks whether or not its working as expected and checks whether __search_query__ returns the correct values after searching for a particular query.
>
> `test_tabulate_it` <br>
> This function tests whether or not __tabulate_it__ function is working as expected and returning a string upon passing valid values.
>
> `test_export_txt` <br>
> This function checks whether or not __export_txt__ function is working as expected and creating a folder named '__txt_exports__' in the same directory and a file named '__filename.txt__' in that folder.
>
> `test_export_txt_errors` <br>
> This function checks whether or not __export_txt__ raises an error upon passing in an invalid file.
>
> `test_export_json` <br>
> This function checks whether or not __export_json__ function is working as expected and creating a folder named '__json_exports__' in the same directory and a file named '__filename.json__' in that folder.
>
> `test_export_json_errors` <br>
> This function checks whether or not __export_json__ raises an error upon passing in an invalid file.
>


## Overview of `view_color.py`
This file contains `tkinter` code and is responsible for the gui part of the program. this file contains only one function which then contains 2 functions of its own.
> ### Functions
> - `display(color_name,color_hex,color_rgb)` <br>
> This function is used by __project.py__ to display a color in a gui window. it takes three parameters.
>   - __color_name__: name of the color
>   - __color_hex__: hex code of the color
>   - __color_rgb__: rgb values of the color
>
>   It then dislpays the color and values in a window.<br>
> This function has 2 functions of its own.
>   - `copy_rgb`: This function copies the RGB values to clipboard using __pyperclip__ module.
>   - `copy_hex`: This function copies the hex value to clipboard using __pyperclip__ module.


## Overview of `database.csv`
__'database.csv'__ was originally named __'color_names.csv'__ that i downloaded from [kaggle](https://www.kaggle.com/). <br>
I removed some columns and added some back. It had 340+ duplicate hex values so i removed them as well. it was a pain to remove the duplicate values but eventually i figured it out and wrote a program to do just that.<br>
Originally it looked like this
```
"Name","Hex (24 bit)","Red (8 bit)","Green (8 bit)","Blue (8 bit)","Hue (degrees)","HSL.S (%)","HSL.L (%), HSV.S (%), HSV.V (%)"
"Absolute zero","#0048BA",0,72,186,217.0,100.0,73.0
"Acid green","#B0BF1A",176,191,26,65.0,76.0,43.0
...
"Zomp","#39A78E",57,167,142,166.0,49.0,44.0
```
After some processing and adding more colors from different sources it now looks like this
```
ID,Name,Hex,Red,Green,Blue
1,Absolute zero,#0048BA,0,72,186
2,Acid green,#B0BF1A,176,191,26
...
1754,Zomp,#39A78E,57,167,142
```
It has a total of __1754 colors__.


## Overview of `test_database.csv`
It is similar to __database.csv__ file except that it has only 10 rows. `test_project.csv` uses this dataset for testing purposes.
```
ID,Name,Hex,Red,Green,Blue
1,Absolute zero,#0048BA,0,72,186
2,Acid green,#B0BF1A,176,191,26
3,Aero,#7CB9E8,124,185,232
4,Aero blue,#C9FFE5,201,255,229
5,African violet,#B284BE,178,132,190
6,Air Force blue (RAF),#5D8AA8,93,138,168
7,Air Force blue (USAF),#00308F,0,48,143
8,Air superiority blue,#72A0C1,114,160,193
9,Alabama crimson,#AF002A,175,0,42
```
This is all data stored in __test_database.csv__.


## Overview of `README.md`
The file you are currently reading is __README.md__. <br>
SURPRISE. <br>
This file contains the information about the whole project. I am creating this file in  __VSCode__ and i'd like you to read the file in a markdown application of your choice which renders its contents. Text version of this file may look a bit cryptic.


## Overview of `requirements.txt`
This file can be used to download __external libraries__ directly using `pip`. <br>
> ### How to use
> Fireup __terminal__ or __cmd prompt__ and change the directory to where the project is located on your computer or laptop.
> ```
> C:\Windows\system32>
> 
> C:\Windows\system32>cd C:\Users\Anas\Downloads\project
> 
> C:\Users\Anas\Downloads\project>
> 
> ```
>Make sure __requirements.txt__ is the this directory.<br>
>Enter this command `pip install -r requirements.txt`
>```
>C:\Users\Anas\Downloads\project>pip install -r requirements.txt
>```
> This will download & install all libraries mentioned in __requirements.txt__ file.


## Overview of `python_icon.ico`
This is the logo of python and is used by `view_color.py` to set as window icon in the title bar.

>![Python Official Logo](.\python_icon.ico)
> 
>This is what it looks like if for some reason you didn't know!

---

## Copyrights
I __DO NOT__ own the `color_names.csv` dataset or the __python logo__ i used in this project. they belong to their respective owners.
