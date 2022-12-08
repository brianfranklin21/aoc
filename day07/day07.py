""" https://adventofcode.com/2022/day/7
"""


class Folder:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0

    def inc_size(self, file_size):
        self.size += file_size
        if self.parent is not None:
            self.parent.inc_size(file_size)


class DaySeven:

    def __init__(self, input_fname):
        self.folders = {}
        cwd = []
        with open(input_fname, 'r') as _file:
            for line in _file:
                line = line.strip()

                if "$ cd " in line:
                    if "$ cd /" == line:
                        cwd = ["/", ]
                        if "/" not in self.folders:
                            self.folders["/"] = Folder("/", None)
                    elif "$ cd .." == line:
                        cwd.pop()
                    else:  # $ ch <name>
                        name = line.split()[-1]
                        cwd.append(name)
                        if "/".join(cwd) not in self.folders:
                            folder = Folder(name, self.folders["/".join(cwd[0:-1])])
                            self.folders["/".join(cwd)] = folder

                elif "$ ls" in line:
                    continue

                elif "dir " in line:
                    continue

                else:  # it's a file
                    size, name = line.split()
                    self.folders["/".join(cwd)].inc_size(int(size))

    def part1(self):
        """ Find all of the directories with a total size of at most 100000.
            What is the sum of the total sizes of those directories?
        """
        # print("All Folders:", [(f.name, f.size) for f in self.folders.values()])
        # print("Folders <= 100000:",
        #       [(f.name, f.size) for f in self.folders.values() if f.size <= 100000])
        print(sum([f.size for f in self.folders.values() if f.size <= 100000]))

    def part2(self):
        """
        """
        print()


# day7 = DaySeven("sample.txt")
day7 = DaySeven("input.txt")
day7.part1()
day7.part2()
