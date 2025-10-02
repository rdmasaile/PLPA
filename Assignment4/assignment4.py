# File processing

words = 0
lines = []

try:
    with open('input.txt', 'r') as f:
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
    print("Error: 'input.txt' file not found.")
    lines = []
    words = []




