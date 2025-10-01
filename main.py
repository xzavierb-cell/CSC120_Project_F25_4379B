game_name = "Xetra"
print("Greetings, Welcome to", game_name, "!")
print("================================")
print("Before we begin, what is your characters's name?")

c_name = input()
print("Great,", c_name + "!", "Let's begin the adventure!")

player = {
    "name": c_name,
    "health": 100,
    "coin": 0,
}
import random

events = ["find a coin", "meet a monster", "do nothiing"]
event = random.choice(events)
print(f"While exploring, you {event}!")

player = {
    "name": c_name,
    "coin": 5
}
player["coin"] += 1
print(f"Player", c_name, "found a coin", c_name, "now has" {player["coin"]} "coins.")