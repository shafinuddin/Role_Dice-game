
# 🎲 Dice Rolling Simulator

This is a fun, beginner-friendly Python program that simulates the rolling of **two dice** using the `random.randint()` function. The user is greeted with ASCII art and asked if they want to roll the dice. If they say "yes", two random dice values are generated.

## 📸 Preview

```
      ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⠿⠿⠿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ...
Welcome to the Dice Rolling Simulator!
Do you want to roll the dice? (yes/no)
yes
Rolling the dice
⚀ ⚁ ⚂ ⚃ ⚄ ⚅
You rolled 3, 6
```

## 🧠 Features

- Asks the user for permission before rolling
- Rolls **two dice** and shows the result
- Fun ASCII art intro
- Uses `random.randint()` to simulate dice behavior
- Works in any terminal or command prompt

## 🛠️ Requirements

- Python 3.x

## ▶️ How to Run

1. Copy or download the Python script.
2. Open a terminal and navigate to the file location.
3. Run the script using:

```bash
python dice_simulator.py
```

## 📜 Code Summary

```python
import random

print("""
      ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⠿⠿⠿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ...
""")
print("Welcome to the Dice Rolling Simulator!")
print("Do you want to roll the dice? (yes/no)")
user_choice = input().lower()

if user_choice == "yes" or user_choice == "YES":
    print("Rolling the dice")
    print("⚀ ⚁ ⚂ ⚃ ⚄ ⚅")
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print(f"You rolled {dice_1},{dice_2}")
else:
    print("Goodbye!")
```

## 📄 License

This project is licensed under the MIT License. Use and modify freely for learning and fun!
