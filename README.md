# Shooting Game & Space Dodge

## Shooting Game

A two-player spaceship shooting game built using Pygame. Each player controls a spaceship and tries to shoot down the opponent while dodging bullets.

### Features

- Two-player mode (Red vs Yellow Spaceships)
- Health system for each spaceship
- Bullet shooting with collision detection
- Background space theme
- Game restart after a winner is declared

### Controls

#### Yellow Spaceship:

- Move: `W` (Up), `A` (Left), `S` (Down), `D` (Right)
- Shoot: `Left Ctrl`

#### Red Spaceship:

- Move: `Arrow Keys`
- Shoot: `Right Ctrl`

### How to Play

- Move your spaceship using the assigned controls.
- Shoot bullets to hit your opponent.
- Each player has 10 health points.
- The player who reduces the opponent's health to zero first wins.
- The game will restart automatically after a winner is displayed.

### Installation

1. Install Python and Pygame:
   ```bash
   pip install pygame
   ```
2. Place all assets (`spaceship_yellow.png`, `spaceship_red.png`, `space.png`, `Grenade+1.mp3`, `Gun+Silencer.mp3`) inside an `Assets` folder.
3. Run the game:
   ```bash
   python shooting_game.py
   ```

---

## Space Dodge

A single-player survival game where the player dodges falling stars for as long as possible.

### Features

- Endless gameplay with increasing difficulty
- Stars spawn at random locations
- Timer displays how long the player survives

### Controls

- Move Left: `Left Arrow`
- Move Right: `Right Arrow`

### How to Play

- Use arrow keys to move left or right.
- Avoid getting hit by falling stars.
- Survive as long as possible to achieve a high score.
- The game ends when a star hits the player.

### Installation

1. Install Python and Pygame:
   ```bash
   pip install pygame
   ```
2. Place the background image (`bg.jpg`) in the same directory.
3. Run the game:
   ```bash
   python space_dodge.py
   ```

