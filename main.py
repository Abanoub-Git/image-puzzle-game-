import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game Settings
TILE_SIZE = 150
GRID_SIZE = 3
WINDOW_WIDTH = TILE_SIZE * GRID_SIZE
WINDOW_HEIGHT = TILE_SIZE * GRID_SIZE + 40  # Small bottom space

# Colors
WHITE = (255, 255, 255)
BG_TOP = (70, 80, 150)
BG_BOTTOM = (30, 35, 60)
BUTTON_COLOR = (100, 120, 200)
TEXT_COLOR = (50, 50, 50)
HIGHLIGHT = (200, 200, 255)

# Fonts
TITLE_FONT = pygame.font.SysFont("Arial", 40, bold=True)
INSTRUCTION_FONT = pygame.font.SysFont("Arial", 24)
BUTTON_FONT = pygame.font.SysFont("Arial", 24)

# Load image and slice into tiles
def load_image(path):
    image = pygame.image.load(path).convert()
    image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT - 40))
    tiles = []
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            tiles.append(image.subsurface(rect))
    return tiles

# Find blank tile index
def find_blank(grid):
    return grid.index(len(grid) - 1)

# Swap two positions
def swap(grid, i, j):
    grid[i], grid[j] = grid[j], grid[i]

# Handle mouse click
def handle_click(grid, pos):
    mx, my = pos
    click_x = mx // TILE_SIZE
    click_y = my // TILE_SIZE
    idx = click_y * GRID_SIZE + click_x
    blank_idx = find_blank(grid)

    bx, by = blank_idx % GRID_SIZE, blank_idx // GRID_SIZE
    if abs(click_x - bx) + abs(click_y - by) == 1:
        swap(grid, idx, blank_idx)

# Draw puzzle grid
def draw_grid(screen, tiles, grid):
    screen.fill(WHITE)
    for idx, pos in enumerate(grid):
        x = (idx % GRID_SIZE) * TILE_SIZE
        y = (idx // GRID_SIZE) * TILE_SIZE
        if pos == len(grid) - 1:
            pygame.draw.rect(screen, HIGHLIGHT, (x, y, TILE_SIZE, TILE_SIZE))
        else:
            screen.blit(tiles[pos], (x, y))

# Check win condition
def check_win(grid):
    return all(i == pos for i, pos in enumerate(grid))

# Draw vertical gradient background
def draw_gradient_background(screen):
    for y in range(WINDOW_HEIGHT):
        ratio = y / WINDOW_HEIGHT
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (WINDOW_WIDTH, y))

# Start Menu
def start_menu(screen):
    buttons = [
        pygame.Rect(90, 200, 220, 50),
        pygame.Rect(90, 270, 220, 50),
        pygame.Rect(90, 340, 220, 50)
    ]
    selected = None

    while selected is None:
        draw_gradient_background(screen)

        # Title
        title = TITLE_FONT.render("Image Puzzle Game", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        screen.blit(title, title_rect)

        # Instruction
        instruction = INSTRUCTION_FONT.render("Choose an Image to Play", True, WHITE)
        instruction_rect = instruction.get_rect(center=(WINDOW_WIDTH // 2, 145))
        screen.blit(instruction, instruction_rect)

        # Buttons
        for i, rect in enumerate(buttons):
            pygame.draw.rect(screen, BUTTON_COLOR, rect, border_radius=8)
            text = BUTTON_FONT.render(f"Image {i+1}", True, TEXT_COLOR)
            screen.blit(text, text.get_rect(center=rect.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(event.pos):
                        selected = f"assets/image{i+1}.jpg"

        pygame.display.flip()

    return selected

# Main game loop
def play_game(screen, image_path):
    tiles = load_image(image_path)
    grid = list(range(len(tiles)))
    random.shuffle(grid)

    clock = pygame.time.Clock()
    back_button = pygame.Rect(10, WINDOW_HEIGHT - 35, 120, 30)

    running = True
    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return
                else:
                    handle_click(grid, pygame.mouse.get_pos())

        draw_grid(screen, tiles, grid)

        # Draw "Back" button
        pygame.draw.rect(screen, BUTTON_COLOR, back_button, border_radius=5)
        back_text = BUTTON_FONT.render("Back to Menu", True, TEXT_COLOR)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        pygame.display.flip()

        if check_win(grid):
            print("🎉 You solved the puzzle!")
            win_text = BUTTON_FONT.render("You Win!", True, WHITE)
            screen.blit(win_text, (WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT - 30))
            pygame.display.update()
            pygame.time.wait(1500)
            return

# Full game loop
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Puzzle Game")

    while True:
        selected_image = start_menu(screen)
        play_game(screen, selected_image)

if __name__ == "__main__":
    main()