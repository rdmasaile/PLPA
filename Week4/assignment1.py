# File processing

words = 0
lines = []

file_path = input("Enter the path to the input file: ")

try:
    with open(file_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            words += len(line.split())

        # convert to uppercase
        lines = [line.upper() for line in lines]

    lines.append(f'Total words: {words}\n')

    with open('output.txt', 'w') as f:
       f.writelines(lines)

    print("File processing complete. Check 'output.txt' for results.")
except FileNotFoundError:
    print(f"Error: '{file_path}' file not found.")
    lines = []
    words = []
except PermissionError:
    print(f"Error: Permission denied when trying to read '{file_path}'.")
    lines = []
    words = []