# Snowman Meltdown

A terminal-based word guessing game written in Python. Guess the hidden word one letter at a time — but be careful: every wrong guess melts the snowman a little more. Can you save him before he's completely gone?

## How to Play

1. A secret word is chosen at random.
2. Enter one letter per turn to guess the word.
3. Correct letters are revealed in the word; wrong guesses melt the snowman.
4. You have **7 attempts** before the snowman fully melts.
5. After each round you can choose to play again or quit.

## Running the Game

```bash
python snowman.py
```

Requires Python 3. No external dependencies.

## Project Structure

| File | Description |
|---|---|
| `snowman.py` | Entry point — runs the game loop |
| `game_logic.py` | Core logic: word selection and game state |
| `ascii_art.py` | Snowman ASCII art stages |
| `validation_and_messages.py` | Input validation and all user-facing messages |
