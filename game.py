import random

print("Welcome to the Snake, Water, Gun game!")
print("Choices: s = Snake, w = Water, g = Gun")

computer = random.choice(["s", "w", "g"])
you = input("Enter your choice (s/w/g): ").lower()

if you not in ["s", "w", "g"]:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
    exit()

game_map = {"s": 1, "w": -1, "g": 0}
you_val = game_map[you]
computer_val = game_map[computer]

print(f"Computer chose: {computer}")

if you_val == computer_val:
    print("It's a tie!")
elif (you_val == 1 and computer_val == -1) or \
     (you_val == -1 and computer_val == 0) or \
     (you_val == 0 and computer_val == 1):
    print("You win!")
else:
    print("You lose!")