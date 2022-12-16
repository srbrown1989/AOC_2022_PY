class CPU:
    SIGNAL_MARKER = [x for x in range(20, 260, 40)]
    SCREEN_LENGTH = 40

    def __init__(self, instructions):
        self.instructions = instructions
        self.register_X = 1
        self.register_temp = 0
        self.cycle_num = 1
        self.waiting = False
        self.signal_strengths = []
        self.sprite_position = [self.register_X-1, self.register_X, self.register_X+1]
        self.screen = ""

    def next_instruction(self):
        return self.instructions.pop(0)

    def cycle(self):
        self.draw_pixel()
        if self.cycle_num in self.SIGNAL_MARKER:
            self.signal_strengths.append(self.cycle_num * self.register_X)
        self.cycle_num += 1
        if self.waiting:
            self.waiting = False
        else:
            self.register_X += self.register_temp
            self.update_sprite_pos()
            self.register_temp = 0

    def process_instructions(self):
        while len(self.instructions) > 0:
            if not self.waiting:
                instruction = self.instructions.pop(0)
                if 'addx' in instruction:
                    self.process_add(int(instruction[1]))
                else:
                    self.cycle()
        self.print_part_1()

    def process_add(self, number):
        self.register_temp = number
        self.waiting = True
        self.cycle()
        self.cycle()

    def print_part_1(self):
        print(f"\nPart 1:{sum(self.signal_strengths)}")

    def update_sprite_pos(self):
        self.sprite_position = [self.register_X-1, self.register_X, self.register_X+1]

    def draw_pixel(self):
        if (self.cycle_num-1) % 40 in self.sprite_position:
            self.screen += "O"
        else:
            self.screen += "_"
        if len(self.screen) == 40:
            print(self.screen)
            self.screen = ""


with open("data.txt") as file:
    data = [entry.strip().split(' ') for entry in file.readlines()]

cpu = CPU(data)
print("SCREEN:")
cpu.process_instructions()
