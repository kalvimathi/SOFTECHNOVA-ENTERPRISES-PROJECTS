import pygame
import sys

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIN_LINE_COLOR = (0, 255, 0)

# Screen dimensions
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5

# Board setup
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game board (3x3 matrix)
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Game state
player = 1  # 1 for X, 2 for O
game_over = False

def draw_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # Draw X
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:
                # Draw O
                pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                  row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True

def draw_win_line(start_pos, end_pos):
    pygame.draw.line(screen, WIN_LINE_COLOR, start_pos, end_pos, 6)

def check_win(player):
    global game_over

    # Horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            draw_win_line((15, y), (WIDTH - 15, y))
            return True

    # Vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            draw_win_line((x, 15), (x, HEIGHT - 15))
            return True

    # Diagonal win (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_win_line((15, 15), (WIDTH - 15, HEIGHT - 15))
        return True

    # Diagonal win (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] == player:
        draw_win_line((WIDTH - 15, 15), (15, HEIGHT - 15))
        return True

    return False

def restart_game():
    global board, player, game_over
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False
    screen.fill(WHITE)
    draw_lines()

# Game start
screen.fill(WHITE)
draw_lines()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = 2 if player == 1 else 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    draw_figures()
    pygame.display.update()
