import pygame
from board import Board
import random
class Minesweeper(Board):
    def __init__(self, width, height, rect, pos, count_mines, width_w=500, height_w=500):
        super().__init__(width, height, rect, pos)
        pygame.font.init()
        self.width_w = width_w
        self.height_w = height_w
        self.count_mines = count_mines
        self.screen = pygame.display.set_mode((self.width_w, self.height_w))
        self.font = pygame.font.SysFont("calibri", rect[0])
        self.set_mines()
        self.run()

    def set_mines(self):
        if self.count_mines > self.width * self.height // 3 * 2:
            for i in range(len(self.board)):
                self.board[i] = list(map(lambda x: 10, self.board[i]))
            count = 0
            while count != (self.height * self.width) - self.count_mines:
                x = random.randint(0, len(self.board) - 1)
                y = random.randint(0, len(self.board[0]) - 1)
                if self.board[x][y] == 10:
                    self.board[x][y] = -1
                    count += 1
        else:
            count = 0
            while count != self.count_mines:
                x = random.randint(0, len(self.board) - 1)
                y = random.randint(0, len(self.board[0]) - 1)
                if self.board[y][x] == -1:
                    self.board[y][x] = 10
                    count += 1

    def open_cell(self, pos):
        if self.get_cell(pos):
            if self.board[self.get_cell(pos)[0]][self.get_cell(pos)[1]] != 10:
                mines = 0
                i = self.get_cell(pos)[0]
                j = self.get_cell(pos)[1]
                mines += self.re_checker(i - 1, j)
                mines += self.re_checker(i - 1, j - 1)
                mines += self.re_checker(i, j - 1)
                mines += self.re_checker(i + 1, j - 1)
                mines += self.re_checker(i + 1, j)
                mines += self.re_checker(i + 1, j + 1)
                mines += self.re_checker(i, j + 1)
                mines += self.re_checker(i - 1, j + 1)
                self.board[self.get_cell(pos)[0]][self.get_cell(pos)[1]] = mines

    def render(self, screen):
        screen.fill((0, 0, 0))
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == -1:
                    pygame.draw.rect(screen, (255, 255, 255), (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1],
                                                               self.rect[0], self.rect[1]), 1)
                elif self.board[i][j] == 10:
                    pygame.draw.rect(screen, (255, 0, 0),
                                     (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1],
                                      self.rect[0], self.rect[1]), 0)
                else:
                    text = self.font.render(f'{self.board[i][j]}', True, (0, 128, 0))
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1],
                                      self.rect[0], self.rect[1]), 1)
                    screen.blit(text, (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1]))

    def run(self):
        pygame.init()
        running = True
        self.screen.fill((0, 0, 0))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.open_cell(event.pos)
            self.render(self.screen)
            pygame.display.flip()
Minesweeper(5, 5, (40, 40), (0, 0), 25)