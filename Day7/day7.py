from __future__ import annotations


class Directory:
    def __init__(self, name: str, parent: Directory | None) -> None:
        self.name = name
        self.parent = parent or self
        self.subs: dict[str, Directory] = {}
        self.files: dict[str, int] = {}

    def size(self) -> int:
        return sum(d.size() for d in self.subs.values()) + sum(self.files.values())

    def recursive_subs(self) -> set[Directory]:
        return {self}.union(*(sub.recursive_subs() for sub in self.subs.values()))


input = open("data.txt").readlines()

cwd = root = Directory("/", None)
for line in input:
    match line.split():
        case ["$", "cd", "/"]:
            cwd = root
        case ["$", "cd", ".."]:
            cwd = cwd.parent
        case ["$", "cd", sub]:
            cwd = cwd.subs.setdefault(sub, Directory(sub, cwd))
        case ["dir", sub]:
            cwd.subs[sub] = Directory(sub, cwd)
        case [size, file_name] if size.isdecimal():
            cwd.files[file_name] = int(size)

part1_result = sum(d.size() for d in root.recursive_subs() if d.size() <= 100000)
print(f"Part 1: {part1_result}")

size_threshold = 30000000 - 70000000 + root.size()
min_ = root.size()
for d in root.recursive_subs():
    min_ = min(min_, d.size()) if d.size() >= size_threshold else min_
print(f"part 2: {min_}")
