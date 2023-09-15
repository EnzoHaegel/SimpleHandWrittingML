import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Size of each cell (1 pixel as per your request is 64x64 block)
CELL_SIZE = 64

# Load Textures
lamp_on = pygame.image.load(os.path.join("Assets", "redstone_lamp_on.png"))
lamp_off = pygame.image.load(os.path.join("Assets", "redstone_lamp.png"))

# Resize textures to fit our cell size
lamp_on = pygame.transform.scale(lamp_on, (CELL_SIZE, CELL_SIZE))
lamp_off = pygame.transform.scale(lamp_off, (CELL_SIZE, CELL_SIZE))

# Create the screen with a size of 1024x1024 for the 16x16 cells
screen = pygame.display.set_mode((16 * CELL_SIZE, 16 * CELL_SIZE))
pygame.display.set_caption('16x16 Bit Array Display')

def draw_grid(bit_array):
    """Draw the 16x16 array on the pygame window."""
    for y, row in enumerate(bit_array):
        for x, cell in enumerate(row):
            texture = lamp_on if cell == 1 else lamp_off
            screen.blit(texture, (x * CELL_SIZE, y * CELL_SIZE))
    
    # Draw vertical lines
    for x in range(17):  # 17 lines for 16 cells
        pygame.draw.line(screen, (0, 0, 0), (x * CELL_SIZE, 0), (x * CELL_SIZE, 16 * CELL_SIZE))
    
    # Draw horizontal lines
    for y in range(17):  # 17 lines for 16 cells
        pygame.draw.line(screen, (0, 0, 0), (0, y * CELL_SIZE), (16 * CELL_SIZE, y * CELL_SIZE))

def main():
    # Sample 16x16 bit array
    bit_array = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(16)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black to clear previous drawings
        draw_grid(bit_array)
        pygame.display.flip()

if __name__ == "__main__":
    main()
