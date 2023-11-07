# 0x0B. Python - Input/Output
This project will cover the following concepts.
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read file line by line
* How to move the cursor in a file
* How to make sure a file is closed when you're done using it
* What is and how to use the `with` statement
* What is `JSON`
* What is serialization
* How to convert Python data structures into JSON and vice versa

## Short notes Python - Input/Output
`open()` returns a file object. Often used with two positional arguments and one keyword.
`>>> f = open(‘workfile’, ‘w’, encoding=’utf-8’)`

 mode can be `'r'` when the file will only be read, `'w'` for only writing (an existing file with the same name will be erased), and `'a'` opens the file for appending; any data written to the file is automatically added to the end. `'r+'` opens the file for both reading and writing. The mode argument is optional; `'r'` will be assumed if it’s omitted.

To get to open a file without having the trouble of losing data or failing to write some elements. Use the with key from the Python library. 

So you end up writing something like this:
`>>> with open(‘file_name’, ‘w’, encoding=”utf-8”) as f:`

Opening and closing files is very easy on python compared with C. The function `readline()` returns a line while the function `readlines()` returns all the lines in the document.

`tell()` - gives you the cursor position of the file
`seek()` - changes the position of the cursor of the file
`read()` - reads the content of the file
`write()` - writes content into the file

The file can be a text based file or a binary file like jpeg or .exe. Opening these files will be different each time. 

To save complicated data types to files, Python allows you to use the popular data interchange format called JSON(Javascript Object Notation) to take python data hierarchies and convert them to string representation. This process is called serialization.

Reconstructing the string from JSON is called deserialization.
