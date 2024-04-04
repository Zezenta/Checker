# Checker
Checker is a very simple, yet useful tool that will let you count the size of each folder inside a directory, and mark with red those bigger than 1GB.
This will help you check if or which folder is taking too much space in your hard drive.

#Requirements
The only module needed for this program is colorama for the colors in the terminal.
To install colorama using pip, you just have to write
```
pip install colorama
```
in a terminal and you should be good to go.

# Usage
You just have to move the file to the location which you want to check, for example, you can move it to
```
C:\Users\johndoe
```
And then in that folder, start a command line (cmd), and type
```
python checker.py
```
And it'll count the size of each folder inside johndoe.
It works with any folder, just dont forget to copy the file to the folder you want to check its size. You can delete it afterwards.