import pygame
import math
from queue import PriorityQueue
import time

# ─── CONFIG ────────────────────────────────────────────────
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 30, 40
CELL_SIZE = WIDTH // COLS

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GRAY   = (70, 70, 70)
GREEN  = (0, 220, 0)
RED    = (220, 0, 0)
BLUE   = (0, 100, 255)
YELLOW = (255, 220, 0)
PURPLE = (180, 0, 220)

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.color = WHITE
        self.g = float("inf")
        self.f = float("inf")
        self.previous = None
        self.is_wall = False

    def get_pos(self):
        return self.row, self.col

    def make_start(self):
        self.color = BLUE

    def make_end(self):
        self.color = YELLOW

    def make_wall(self):
        self.color = BLACK
        self.is_wall = True

    def make_open(self):
        if not self.is_wall and self.color not in (BLUE, YELLOW):
            self.color = GREEN

    def make_closed(self):
        if not self.is_wall and self.color not in (BLUE, YELLOW):
            self.color = RED

    def make_path(self):
        if not self.is_wall and self.color not in (BLUE, YELLOW):
            self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(win, GRAY, (self.x, self.y, CELL_SIZE, CELL_SIZE), 1)

    def __lt__(self, other):
        return self.f < other.f


def h(p1, p2):
    return math.hypot(p1[1] - p2[1], p1[0] - p2[0])


def a_star(draw_callback, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_hash = {start}

    start.g = 0
    start.f = h(start.get_pos(), end.get_pos())

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            # Final path animation – slower so it's visible
            temp = current
            while temp.previous:
                temp = temp.previous
                if temp != start and not temp.is_wall:
                    temp.make_path()
                    draw_callback()
                    time.sleep(0.08)           # ← clearly see purple path being drawn
            draw_callback()
            return True

        current.make_closed()
        draw_callback()
        time.sleep(0.025)                      # ← closing nodes visible

        for neighbor in current.neighbors:
            if neighbor.is_wall or neighbor.color == RED:
                continue

            cost = 1 if abs(neighbor.row - current.row) + abs(neighbor.col - current.col) == 1 else 1.414
            tentative_g = current.g + cost

            if tentative_g < neighbor.g:
                neighbor.previous = current
                neighbor.g = tentative_g
                neighbor.f = tentative_g + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.f, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
                    draw_callback()
                    time.sleep(0.018)          # ← opening nodes visible

    return False


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("A* WITH obstacles – visible animation")
    clock = pygame.time.Clock()

    grid = [[Node(i, j) for j in range(COLS)] for i in range(ROWS)]

    start = grid[ROWS//2 - 3][3]
    end   = grid[ROWS//2 + 3][COLS-4]
    start.make_start()
    end.make_end()

    # Create some obstacles
    for i in range(ROWS):
        for j in range(COLS):
            if (j == COLS//2 - 6 and 4 < i < ROWS-4) or \
               (j == COLS//2 + 4 and 6 < i < ROWS-6) or \
               (i == ROWS//2 - 5 and 10 < j < COLS-12) or \
               (i == ROWS//2     and 12 < j < COLS-10) or \
               (i == ROWS//2 + 5 and 8  < j < COLS-14):
                grid[i][j].make_wall()

    # Precompute 8-direction neighbors
    for i in range(ROWS):
        for j in range(COLS):
            node = grid[i][j]
            node.neighbors = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < ROWS and 0 <= nj < COLS:
                        node.neighbors.append(grid[ni][nj])

    found = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                if event.key == pygame.K_r and found:
                    pygame.quit()
                    return main()
                if event.key == pygame.K_SPACE and not found:
                    def draw():
                        win.fill((18, 18, 32))
                        for row in grid:
                            for node in row:
                                node.draw(win)
                        pygame.display.flip()

                    found = a_star(draw, grid, start, end)

        # Continuous drawing
        win.fill((18, 18, 32))
        for row in grid:
            for node in row:
                node.draw(win)

        font = pygame.font.SysFont("segoeui", 24)
        if not found:
            txt = font.render("Press SPACE → watch A* search & path", True, (220, 220, 255))
            win.blit(txt, (WIDTH//2 - txt.get_width()//2, 20))
        else:
            txt = font.render("Path found – press R to restart", True, (120, 255, 160))
            win.blit(txt, (WIDTH//2 - txt.get_width()//2, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()