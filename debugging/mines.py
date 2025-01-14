#!/usr/bin/python3
import random
import os

# Function to clear the screen, supporting different operating systems.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        # Initialize game parameters
        self.width = width
        self.height = height
        if mines > width * height:
            raise ValueError("Too many mines for the field size")  # Ensure valid mine count
        self.mines = set(random.sample(range(width * height), mines))  # Place mines
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Game board
        self.revealed = [[False for _ in range(width)] for _ in range(height)]  # Track revealed cells

    # Print the board, optionally revealing mines
    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Show mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Show mine count
                else:
                    print('.', end=' ')  # Hide cell
            print()

    # Count the number of mines around a given cell
    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    # Reveal a cell and its neighbors iteratively
    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False  # Game over if a mine is revealed
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if self.revealed[cy][cx]:
                continue
            self.revealed[cy][cx] = True
            if self.count_mines_nearby(cx, cy) == 0:  # If no adjacent mines, reveal neighbors
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            stack.append((nx, ny))
        return True

    # Main game loop
    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):  # Check for valid coordinates
                    print("Coordinates out of bounds. Try again.")
                    continue
                if not self.reveal(x, y):  # Reveal cell and check for game over
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:  # Handle invalid input
                print("Invalid input. Please enter numbers only.")

# Run the game
if __name__ == "__main__":
    game = Minesweeper()
    game.play()