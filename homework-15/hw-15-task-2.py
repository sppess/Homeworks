# Write a function called new_lines that takes a file path, opens the file
# and adds a newline character (\n) once in 20 symbols


def new_lines(path):
    with open(path, 'r') as file:
        text = ''.join(['\n' if (index % 20 == 0) else ch for
                          index, ch in enumerate(file.read(), start=1)])
        with open(path, 'w') as new_file:
            new_file.write(text)

    return f"file changes completed"


print(new_lines("task-2-test/textfile1.txt"))
