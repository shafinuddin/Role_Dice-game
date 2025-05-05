import random
print("""
      ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⠿⠿⠿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣾⡿⠟⠉⠁⠀⠀⣠⠶⠒⠙⠛⠿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⡿⠋⠀⠀⠤⣄⣀⣰⠃⠀⠀⠀⠀⠀⠈⠻⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⡿⡡⠖⠋⠙⠲⣄⠐⢻⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⡟⠁⠀⠀⠀⠀⠈⢳⠈⢧⠀⠀⣾⣿⡆⠀⠀⠀⠸⣿⡇⠀⠀⣠⣴⣶⣄
⠀⠀⣿⣿⠃⠀⠀⠀⢀⣀⠀⠘⣿⡿⢷⣄⠘⠛⡃⠀⠰⠀⠀⣿⣇⣴⡾⠟⠋⢹⣿
⠀⠀⢿⣿⡇⠀⠀⠀⢿⣿⡇⠀⢿⣴⣾⡿⠀⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠀⢸⣿
⠀⠀⠘⣿⣧⠀⠀⠀⠈⠩⠥⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠀⣿⡟
⠀⠀⠀⠘⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠽⠁⠀⠀⠀⠀⠀⣾⡿⠁
⠀⠀⠀⠀⠀⣹⣿⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠤⠊⠁⠀⠘⣷⡀⠀⣠⣾⡿⠁⠀
⠀⠀⢀⣴⣾⠿⠋⠀⠉⠉⠛⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠋⠀⠀⠀
⣠⣶⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⠀⠀⠀⠀
⢿⣿⣄⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀
⠀⠙⠿⢿⣶⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⣿⣇⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣾⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⡟⠛⠛⠿⣷⣄⣀⣀⣀⣀⣀⣀⣴⡾⠟⠋⢉⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⠿⣶⣶⣶⠿⠿⠿⠿⠿⠿⠻⠿⠿⠷⠶⠶⠿⠟⠁⠀⠀⠀⠀""")
print("Welcome to the Dice Rolling Simulator!")
print("Do you want to roll the dice? (yes/no)")
user_choice=input().lower()
if user_choice=="yes" or user_choice=="YES":
    print("Rolling the dice")
    print("""⚀ ⚁ ⚂ ⚃ ⚄ ⚅""")
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    print(f"You rolled {dice_1},{dice_2}")
else:
    print("Goodbye!")
# The code simulates a dice rolling game. It prompts the user to roll the dice and generates two random numbers between 1 and 6, representing the dice rolls. The results are displayed in a formatted manner.