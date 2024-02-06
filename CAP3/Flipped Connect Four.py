import numpy as np , pygame , sys
# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Flipped Connect Four')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Define colors
MINT = (170, 255, 170)
WHITE = (255, 255, 255)
PINK = (255, 85, 255)
BLUE = (0, 170, 255)

# Define board dimensions
R_COUNT = 6
C_COUNT = 7

# Function to create an empty board
def create_board():
    return np.zeros((R_COUNT, C_COUNT))

# Function to drop a piece onto the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check if a column is a valid location to drop a piece
def is_valid_location(board, col):
    return board[R_COUNT - 1][col] == 0

# Function to find the next open row in a column
def get_next_open_row(board, col):
    return np.argmax(board[:, col] == 0)

# Function to print the board
def print_board(board):
    print(np.flip(board, 0))

# Function to check if a player has won the game
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(C_COUNT - 3):
        for r in range(R_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(C_COUNT):
        for r in range(R_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(C_COUNT - 3):
        for r in range(R_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(C_COUNT - 3):
        for r in range(3, R_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

# Function to draw the board on the screen
def draw_board(screen, board, SQUARESIZE, RADIUS):
    for c in range(C_COUNT):
        for r in range(R_COUNT):
            pygame.draw.rect(screen, MINT, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c] == 1:
                pygame.draw.circle(screen, PINK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, BLUE, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

# Main function to run the game
def main():
    # Initialize the game board and display
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100
    width = C_COUNT * SQUARESIZE
    height = (R_COUNT + 1) * SQUARESIZE
    size = (width, height)
    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(screen, board, SQUARESIZE, RADIUS)

    myfont = pygame.font.SysFont("CG Times", 55)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # Clear the area above the board
                pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]  # Get the x-coordinate of the mouse position
                if turn == 0:
                    # Draw a pink game piece at the current mouse position
                    pygame.draw.circle(screen, PINK, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    # Draw a blue game piece at the current mouse position
                    pygame.draw.circle(screen, BLUE, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Clear the area above the board
                pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]  # Get the x-coordinate of the mouse position
                col = int(posx // SQUARESIZE)  # Calculate the column where the piece should be dropped

                # Check if the selected column is a valid move
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)  # Find the next available row in the selected column
                    drop_piece(board, row, col, turn + 1)  # Drop the game piece into the selected column

                    # Check if the current player has won
                    if winning_move(board, turn + 1):
                        # Render and display the winning message
                        label = myfont.render(f"CONTENDER {turn + 1} WINS!;D", 1, PINK if turn == 0 else BLUE)
                        screen.blit(label, (60, 20))
                        game_over = True  # Set the game_over flag to True

                    draw_board(screen, board, SQUARESIZE, RADIUS)  # Redraw the game board with the new move

                    # Switch turns between players
                    turn += 1
                    turn %= 2

                    if game_over:
                        pygame.time.wait(2000)  # Wait for 5 seconds before exiting


if __name__ == "__main__":
    main()
