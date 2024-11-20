import random


class Cell:

    def __init__(self, around_mines: int, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
        self.flag = False


class GamePole:

    def __init__(self, n: int, mines: int):
        self.n = n
        self.m = mines
        self.pole = [[Cell(0, False) for _ in range(self.n)] for _ in range(self.n)]

        self.flag_count = 0

        self.set_mines()
        self.count_around_mines()
        self.event_loop()

    def set_mines(self):
        mines = random.sample(range(self.n * self.n), self.m)
        for mine in mines:
            i = mine // self.n
            j = mine % self.n
            self.pole[i][j].mine = True

    def count_around_mines(self):
        for i in range(self.n):
            for j in range(self.n):
                if not self.pole[i][j].mine:
                    count = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if x == 0 and y == 0:
                                continue
                            if i + x < 0 or i + x >= self.n or j + y < 0 or j + y >= self.n:
                                continue
                            if self.pole[i + x][j + y].mine:
                                count += 1
                    self.pole[i][j].around_mines = count

                    if count == 0:
                        self.pole[i][j].fl_open = True

    def show(self):
        print("\033c", end="")
        print(self.m - self.flag_count, "mines left")
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].flag:
                    print("M", end=" ")
                    continue
                if self.pole[i][j].fl_open:

                    if self.pole[i][j].mine:
                        print("*", end=" ")
                    else:
                        print(self.pole[i][j].around_mines, end=" ")
                else:
                    print("#", end=" ")
            print()

    def open_cell(self, i: int, j: int):
        if self.pole[i][j].mine:
            raise Exception("Game over")
        else:
            self.pole[i][j].fl_open = True
            if self.pole[i][j].flag:
                self.flag_count -= 1
                self.pole[i][j].flag = False

    def flag_cell(self, i: int, j: int):
        if self.m != self.flag_count:
            self.pole[i][j].flag = True
            self.flag_count += 1

    def event_loop(self):
        while True:
            try:
                self.show()

                if self.check_win():
                    print("You win!")
                    break

                user_input = input("Enter cell: ").strip().split()

                if len(user_input) < 2 or len(user_input) > 3:
                    continue

                try:
                    i, j = int(user_input[0]) - 1, int(user_input[1]) - 1
                except ValueError:
                    continue

                if i < 0 or i >= self.n or j < 0 or j >= self.n:
                    continue

                if len(user_input) == 2:
                    if not self.pole[i][j].fl_open:
                        self.open_cell(i, j)

                elif len(user_input) == 3 and user_input[2].lower() == 'm':
                    if not self.pole[i][j].fl_open and not self.pole[i][j].flag:
                        self.flag_cell(i, j)

            except Exception:
                self.loss()
                break

    def check_win(self):
        if self.m == self.flag_count:
            for i in range(self.n):
                for j in range(self.n):
                    if self.pole[i][j].mine and not self.pole[i][j].flag:
                        return False
                    if not self.pole[i][j].mine and self.pole[i][j].flag:
                        return False
            return True

    def loss(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].mine:
                    self.pole[i][j].fl_open = True
        self.show()
        print("Game over")


pole_game = GamePole(6, 10)



