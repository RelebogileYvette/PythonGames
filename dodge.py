import pygame
import time
import random

# Initialize pygame
pygame.font.init()

# Define dimensions
WIDTH, HEIGHT = 800, 600

# Create the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Pass as a tuple
pygame.display.set_caption('Space Dodge')

BG = pygame.image.load('bg.jpg')

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars):
    """
    Draws all game elements onto the screen.

    Args:
        player (pygame.Rect): The player's rectangular object.
        elapsed_time (float): The time elapsed since the start of the game.
        stars (list): A list of rectangular star objects.
    """
    WIN.blit(BG, (0, 0))  # Draw the background

    # Display the elapsed time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", True, "white")
    WIN.blit(time_text, (10, 10))

    # Draw the player rectangle
    pygame.draw.rect(WIN, "red", player)

    # Draw all stars
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    # Update the display
    pygame.display.update()

def main():
    """
    Main game loop to handle game logic, input, and rendering.
    """
    running = True

    # Initialize the player as a rectangular object
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    # Track time and star spawn intervals
    start_time = time.time()
    elapsed_time = 0

    star_add_increament = 2000
    star_count = 0

    stars = []  # List to store all active stars
    hit = False  # Flag to indicate if the player has been hit

    while running:
        # Increment the star spawn timer
        star_count += clock.tick(60)
        clock.tick(60)  
        elapsed_time = time.time() - start_time  # Calculate elapsed time

        # Add new stars after the interval
        if star_count > star_add_increament:
            for _ in range(3):  # Add 3 stars at once
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            # Gradually decrease the interval to add difficulty
            star_add_increament = max(200, star_add_increament - 50)
            star_count = 0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                running = False
                break

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Update star positions and check for collisions
        for star in stars[:]:
            star.y += STAR_VEL  # Move the star downward
            if star.y > HEIGHT:
                stars.remove(star)  # Remove stars that go off-screen
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)  # Remove the colliding star
                hit = True  # Player is hit
                break

        # Handle game over if player is hit
        if hit:
            lost_text = FONT.render("Sorry You Lost!", True, "white")
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)  # Display the game over message for 4 seconds
            break

        # Draw all elements
        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()
