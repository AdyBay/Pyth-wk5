def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Line 3 with some special characters: @#$%\n")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File creation process completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is line 7\n")
            file.write("78432\n")
            file.write("Line 8 with additional content\n")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File appending process completed.")

def main():
    create_file()
    read_file()
    append_to_file()

if __name__ == "__main__":
    main()
