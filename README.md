# Alien Invasion Game

Alien Invasion is a classic arcade-style game developed using Python and the Pygame library. The objective is to shoot down waves of aliens while avoiding their attacks. The game becomes progressively more challenging as you advance through levels.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Features](#features)


## Installation

To get started with Alien Invasion, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/alien-invasion.git
   cd alien-invasion
2. Create a virtual environment (optional but recommended):
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required dependencies:
    pip install -r requirements.txt
4. Run the game:
    python alien_invasion.py

## How to Play

Welcome to Alien Invasion! The goal of the game is to shoot down waves of aliens while avoiding their attacks. Here's how you can play:

## Controls

- **Move Left:** Use the **left arrow key** to move your ship to the left.
- **Move Right:** Use the **right arrow key** to move your ship to the right.
- **Shoot:** Press the **spacebar** to fire bullets at the incoming aliens.
- **Quit:** Press the **'q' key** to quit the game at any time.

## Objective

- Your objective is to eliminate all the aliens before they reach the bottom of the screen.
- Avoid collisions with the aliens, as each collision will result in losing a life.
- The game ends when you lose all your lives.

## Game Flow

- The game starts when you press the "Play" button.
- Each level increases the difficulty, with faster and more numerous aliens.
- When all aliens are destroyed, you advance to the next level, and the challenge increases.

## Scoring

- Points are awarded for each alien you shoot down.
- Try to beat your high score by surviving as many levels as possible.

## Project Structure


alien_invasion.py          # Main game loop and class
settings.py                # Settings and configuration for the game
game_stats.py              # Game statistics tracking
scoreboard.py              # Display and update game score, levels, and lives
button.py                  # Play button implementation
ship.py                    # Player's ship logic
bullet.py                  # Bullet logic
alien.py                   # Alien logic
README.md                  # This file

## Features
Alien Invasion includes a variety of features to enhance your gaming experience:

- **Fullscreen Mode:** The game launches in fullscreen, immersing you in the action.
- **Score Tracking:** Keep track of your current score, high score, and level throughout the game.
- **Responsive Controls:** Enjoy smooth and responsive controls for a seamless gameplay experience.
- **Multiple Levels:** The difficulty increases as you advance through the levels, with more and faster aliens.
- **Pause and Resume:** The game automatically pauses when inactive and can be resumed by clicking the "Play" button.
- **Dynamic Difficulty:** As you progress, the game dynamically adjusts the speed and number of aliens to keep the challenge engaging.
- **High Score System:** Compete against your previous best scores and strive to set new records.
