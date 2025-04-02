def read_and_modify_file():
    """Reads a file, modifies its content, and writes to a new file."""
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
            
        modified_content = [line.upper() for line in content]  # Example modification: Convert text to uppercase
        new_filename = "modified_" + filename
        
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)
        
        print(f"File has been modified and saved as {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You do not have access to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()