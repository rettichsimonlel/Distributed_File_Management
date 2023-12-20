class FileHandler():
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def write_file(self, lines):
        with open(self.file_name, 'w') as file:
            file.writelines(lines)

    def display_content(self):
        lines = self.read_file()
        print(f"Content of {self.file_name}:")
        print(''.join(lines))

    def add_content(self, text):
        lines = self.read_file()
        lines.append(text + '\n')
        self.write_file(lines)
        print(f"Added '{text}' to {self.file_name}")

    def delete_content_by_line_number(self, line_number):
        lines = self.read_file()
        if 0 <= line_number < len(lines):
            del lines[line_number]
            self.write_file(lines)
            print(f"Deleted line {line_number + 1} from {self.file_name}")
        else:
            print("Invalid line number")

    @staticmethod
    def delta_update(file1, file2):
        handler1 = FileHandler(file1)
        handler2 = FileHandler(file2)

        lines_file1 = handler1.read_file()
        lines_file2 = handler2.read_file()

        additional_code = [line for line in lines_file2 if line not in lines_file1]

        for line in additional_code:
            if line in lines_file2:
                line_number = lines_file2.index(line)
                if line not in lines_file1:
                    lines_file1.insert(line_number, line)

        handler1.write_file(lines_file1)
        print(f"Delta update performed. {file1} has been updated with additional content from {file2}.")

file_handler = FileHandler('static/file1.txt')
file_handler.display_content()

file_handler.add_content("New line added")
file_handler.display_content()

file_handler.delete_content_by_line_number(2)
file_handler.display_content()

FileHandler.delta_update('static/file1.txt', 'static/file2.txt')
