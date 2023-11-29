file_path = 'pyyttonRojekti\data3.log'  

try:
    with open(file_path, 'r') as file:
        first_line = file.readline()
        print(first_line)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")