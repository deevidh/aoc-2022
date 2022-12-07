from dave_utils import puzzle

class Dir:
    def __init__(self, name):
        self.name=name
        self.files = {}
        self.dirs = {}

    def add_file(self, name, size):
        self.files[name] = size

    def add_dir(self, name):
        self.dirs[name] = Dir(name)

    def get_dir(self, name):
        return self.dirs[name]

    def get_all_dirs(self):
        all_dirs = []
        for name, dir in self.dirs.items():
            all_dirs.append(dir)
            all_dirs.extend(dir.get_all_dirs())
        return all_dirs

    def get_size(self):
        files_size = sum(self.files.values())
        dirs_size = sum([dir.get_size() for name, dir in self.dirs.items()])
        return files_size+dirs_size

def process_commands(input):
    cwd = []
    for line in input:
        command = line.split()
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '/':
                    cwd.append(Dir('/'))
                elif command[2] == '..':
                    cwd.pop()
                else:
                    # Warning: this assumes that the dir has already been 'created' by ls
                    cwd.append(cwd[-1].get_dir(command[2]))
            if command[1] == 'ls':
                pass
        if command[0] == 'dir':
            cwd[-1].add_dir(command[1])
        if command[0].isdigit():
            cwd[-1].add_file(command[1], int(command[0]))
    return cwd[0]

def part1(input):
    filesystem = process_commands(input)
    return sum([dir.get_size() for dir in filesystem.get_all_dirs() if dir.get_size()<100000])

def part2(input):
    filesystem = process_commands(input)
    required_space = 30000000 - (70000000-filesystem.get_size())
    return sorted([dir.get_size() for dir in filesystem.get_all_dirs() if dir.get_size()>required_space])[0]

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,95437)
my_puzzle.test(part1,95437)

## Part 2
#my_puzzle.test_and_submit(part2,24933642)
my_puzzle.test(part2,24933642)