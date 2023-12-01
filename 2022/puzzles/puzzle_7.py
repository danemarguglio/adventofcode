from pathlib import Path


class Directory:
    def __init__(self, name, parent=None, children={}, size=0):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size

    def get_size(self):
        # calculate sie of self + children folders
        size = self.size
        for i in self.children:
            size += self.children[i].get_size()
        self.size = size
        return size

    def get_children_of_size(self, size):
        # get all folders with less than size size
        results = set()
        for i in self.children.values():
            # skip files
            if not i.children:
                continue
            if i.size <= size:
                results.add(i)
            results.update(i.get_children_of_size(size))
        return results

    def get_all_children(self):
        # set of all folders in children
        results = set()
        for i in self.children.values():
            # skip files
            if not i.children:
                continue
            results.add(i)
            results.update(i.get_all_children())
        return results

    def __repr__(self):
        return f"{self.name} - {self.size} -> {[i for i in self.children]}"


class Terminal:
    def __init__(self):
        self.dir = Directory(name='/', parent=None, children={})
        self.pwd = self.dir

    def is_command(self, line):
        return line[0] == '$'

    def parse_line(self, line):
        if line == '\n':
            return
        if self.is_command(line):
            self.parse_command(line)
        else:
            self.parse_output(line)

    def parse_output(self, line):
        a, b = line.split()
        if a == 'dir':
            if b not in self.pwd.children:
                # Folder, 0 size
                self.pwd.children[b] =  Directory(b, self.pwd, {}, 0)
        else:
            # We have a file, add it with its size
            self.pwd.children[b] = Directory(b, self.pwd, {}, int(a))
    
    def parse_command(self, line):
        # Remove the $ and space
        line = line[2:].strip()

        commands = line.split(' ')
        if commands[0] == 'cd':
            self.cd(commands[1])
        elif commands[0] == 'ls':
            pass
        else:
            raise Exception('Unknown command')

    def cd(self, newdir):
        if newdir == '/':
            self.pwd = self.dir
        elif newdir == '..':
            self.pwd = self.pwd.parent
        else:
            self.pwd = self.pwd.children[newdir]
    

if __name__ == "__main__":
    input_file = Path("../input/input_7.txt")

    result_1 = 0
    result_2 = 0

    with open(input_file, 'r') as f:
        terminal = Terminal()

        for idx, line in enumerate(f):
            terminal.parse_line(line)
        terminal.dir.get_size()


        result_1 = sum([i.size for i in terminal.dir.get_children_of_size(100000)])

        free_space = 70000000 - terminal.dir.size
        needed_space =  30000000 - free_space
        smallest = float('inf')
        for i in terminal.dir.get_all_children():
            if i.size >= needed_space and i.size < smallest:
                smallest = i.size 
        result_2 = smallest


        print(f"Result 1: {result_1}")
        print(f"Result 2: {result_2}")
        
