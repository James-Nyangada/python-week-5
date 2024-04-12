import os

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "my_file.txt")
    
    with open(file_path, "w") as file:
        file.write("My name is James\n")
        file.write("I am 30 years old\n")
        file.write("Another line with some text and numbers: 67890\n")
except FileNotFoundError:
    print("File not found or cannot be created.")
except PermissionError:
    print("Permission denied to create or write to the file.")
else:
    print("File created successfully and content written.")
# Task: File Reading and Display
# Enhance your script to read the contents of "my_file.txt" and display them on the console.

try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found or cannot be opened for reading.")
except PermissionError:
    print("Permission denied to open the file.")

# Task: File Appending
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.

try:
    with open("my_file.txt", "a") as file:
        file.write("Line appended 1\n")
        file.write("Line appended 2\n")
        file.write("Line appended 3\n")
except FileNotFoundError:
    print("File not found or cannot be opened for appending.")
except PermissionError:
    print("Permission denied to append to the file.")

try:
    with open("non_existing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("End of file handling.")
