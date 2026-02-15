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

# ─── NODE ──────────────────────────────────────────────────
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

    def get_pos(self):
        return self.row, self.col

    def make_start(self):
        self.color = BLUE

    def make_end(self):
        self.color = YELLOW

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(win, GRAY, (self.x, self.y, CELL_SIZE, CELL_SIZE), 1)

    def __lt__(self, other):
        return self.f < other.f


# ─── HEURISTIC ─────────────────────────────────────────────
def h(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return math.hypot(c1 - c2, r1 - r2)  # Euclidean (nice for no obstacles)


def a_star(draw, grid, start, end):
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
            # Path animation – slower and clearer
            temp = current
            while temp.previous:
                if temp != start:
                    temp.make_path()
                    draw()
                    pygame.display.flip()   # important!
                    time.sleep(0.06)        # ← increased
                temp = temp.previous
            return True

        current.make_closed()
        draw()
        pygame.display.flip()
        time.sleep(0.018)               # ← was 0.006 – now visible wave

        for neighbor in current.neighbors:
            if neighbor.color == RED:   # closed
                continue

            dist = math.hypot(neighbor.col - current.col, neighbor.row - current.row)
            tentative_g = current.g + dist

            if tentative_g < neighbor.g:
                neighbor.previous = current
                neighbor.g = tentative_g
                neighbor.f = tentative_g + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.f, count, neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end:
                        neighbor.make_open()
                        draw()
                        pygame.display.flip()
                        time.sleep(0.012)   # ← was 0.004 – now you see expansion

    return False


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("A* – NO obstacles – visible animation")
    clock = pygame.time.Clock()

    grid = [[Node(i, j) for j in range(COLS)] for i in range(ROWS)]

    start = grid[ROWS//2][4]
    end   = grid[ROWS//2][COLS-5]
    start.make_start()
    end.make_end()

    # Neighbors (8 directions)
    for i in range(ROWS):
        for j in range(COLS):
            node = grid[i][j]
            node.neighbors = []
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di == 0 and dj == 0: continue
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
                if event.key == pygame.K_r:
                    pygame.quit()
                    return main()
                if event.key == pygame.K_SPACE and not found:
                    found = a_star(
                        lambda: (win.fill((20,20,35)),
                                 *[n.draw(win) for row in grid for n in row],
                                 pygame.display.flip()),
                        grid, start, end
                    )

        # Draw everything every frame
        win.fill((20, 20, 35))
        for row in grid:
            for node in row:
                node.draw(win)

        font = pygame.font.SysFont("segoeui", 24)
        if not found:
            txt = font.render("Press SPACE → watch A* animation", True, (200, 220, 255))
            win.blit(txt, (WIDTH//2 - txt.get_width()//2, 20))
        else:
            txt = font.render("Path complete – press R to restart", True, (100, 255, 140))
            win.blit(txt, (WIDTH//2 - txt.get_width()//2, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()