import pygame
import heapq
import math
import time

# === SETTINGS ===
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 28, 28
CELL = WIDTH // ROWS

BLACK   = (12, 12, 18)
WHITE   = (245, 245, 245)
GRAY    = (70, 70, 85)
GREEN   = (90, 220, 120)     # processing / inconsistent
RED     = (220, 90, 90)      # finalized
BLUE    = (70, 140, 255)     # start
YELLOW  = (255, 220, 100)    # goal
PURPLE  = (190, 100, 255)    # path

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))
pygame.display.set_caption("Simple D* Lite")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)

# === NODE ===
class Node:
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.g   = float('inf')
        self.rhs = float('inf')
        self.color = WHITE
        self.wall  = False
        self.prev  = None

    def pos(self):
        return self.r, self.c

    def __lt__(self, other):
        # very simple tie-breaking
        h_self  = heuristic(self.pos(), goal.pos())
        h_other = heuristic(other.pos(), goal.pos())
        return (min(self.g, self.rhs) + h_self, self.r, self.c) < \
               (min(other.g, other.rhs) + h_other, other.r, other.c)

# === HELPERS ===
def heuristic(a, b):
    dx = abs(a[1] - b[1])
    dy = abs(a[0] - b[0])
    return max(dx, dy) + (math.sqrt(2)-1) * min(dx, dy)

def cost(a, b):
    dr = abs(a.r - b.r)
    dc = abs(a.c - b.c)
    return 1 if dr + dc == 1 else 1.414

def neighbors(r, c):
    res = []
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr == 0 and dc == 0: continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                res.append(grid[nr][nc])
    return res

def update_rhs(u):
    if u is goal:
        u.rhs = 0
        return
    minv = float('inf')
    for v in neighbors(u.r, u.c):
        if v.wall: continue
        minv = min(minv, v.g + cost(u, v))
    u.rhs = minv

# === D* LITE - very simplified version ===
def run_dstarlite():
    pq = []

    # reset
    for row in grid:
        for cell in row:
            cell.g = float('inf')
            cell.rhs = float('inf')
            cell.prev = None
            cell.color = BLACK if cell.wall else WHITE

    goal.rhs = 0
    goal.color = YELLOW
    start.color = BLUE

    heapq.heappush(pq, goal)
    seen = set([goal])

    while pq:
        u = heapq.heappop(pq)
        seen.remove(u)

        if u.g > u.rhs:             # decrease g
            u.g = u.rhs
            u.color = RED
            draw()
            time.sleep(0.015)

            for v in neighbors(u.r, u.c):
                if v.wall: continue
                old_rhs = v.rhs
                update_rhs(v)
                if v.rhs != old_rhs:
                    v.prev = u if v.g > v.rhs else v.prev
                    if v not in seen:
                        heapq.heappush(pq, v)
                        seen.add(v)
                    v.color = GREEN
                    draw()
                    time.sleep(0.008)

        else:                       # increase g
            old_g = u.g
            u.g = float('inf')
            update_rhs(u)
            if u.g != old_g:
                u.color = GREEN
                draw()
                time.sleep(0.012)

            for v in neighbors(u.r, u.c):
                if v.wall: continue
                old_rhs = v.rhs
                update_rhs(v)
                if v.rhs != old_rhs:
                    v.prev = u if v.g > v.rhs else v.prev
                    if v not in seen:
                        heapq.heappush(pq, v)
                        seen.add(v)
                    v.color = GREEN
                    draw()
                    time.sleep(0.008)

    # extract path
    if start.g == float('inf'):
        return False

    cur = start
    while cur and cur is not goal:
        if cur is not start:
            cur.color = PURPLE
        cur = cur.prev
        draw()
        time.sleep(0.04)

    return True

# === DRAW ===
def draw(status="Press SPACE"):
    screen.fill(BLACK)
    for r in range(ROWS):
        for c in range(COLS):
            node = grid[r][c]
            x, y = c*CELL, r*CELL
            pygame.draw.rect(screen, node.color, (x, y, CELL, CELL))
            if not node.wall:
                pygame.draw.rect(screen, GRAY, (x, y, CELL, CELL), 1)

    txt = font.render(status, True, (210,220,255))
    screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT + 18))
    pygame.display.flip()

# === CREATE GRID + SIMPLE MAZE ===
grid = [[Node(r,c) for c in range(COLS)] for r in range(ROWS)]

# border + some walls
for r in range(ROWS):
    for c in range(COLS):
        n = grid[r][c]
        if r in (0,ROWS-1) or c in (0,COLS-1):
            n.wall = True
        elif (r == 10 and 4 < c < 24) or \
             (c == 14 and 6 < r < 22) or \
             (r == 18 and 8 < c < 20):
            n.wall = True

start = grid[2][2]
goal  = grid[ROWS-3][COLS-3]

start.wall = False
goal.wall  = False

# === MAIN LOOP ===
running = True
done = False

draw("Press SPACE to run simple D* Lite")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and not done:
                done = run_dstarlite()
                draw("Path found!" if done else "No path :(")
            if event.key == pygame.K_r:
                pygame.quit()
                # re-run script or implement reset

    if not done:
        draw("Press SPACE to run simple D* Lite")
    clock.tick(60)

pygame.quit()