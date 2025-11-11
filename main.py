import random

game_name = "Xetra"
print("Greetings, Welcome to", game_name, "!")
print("================================")
print("Before we begin, what is your characters's name?")

name = "Tester"
print("Great,", name + "!", "Let's begin the adventure!")

events = ["find a coin", "meet a monster", "do nothiing"]

map_size = 9

player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}

def check_event():
    global events
    global player
    event = random.choice(events)
    if event == "find a coin":
        player["coin"] += 1
    elif event == "meet a monster":
        player["health"] -= 10

def draw_ui(x, y):
    global player, map_size
    print("=" * (map_size * 2 + 5))
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end=" ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end=" ")
            else:
                print(".", end=" ")
        print()
    print("=" * (map_size * 2 + 5))
    print(f"Health: {player['health']}")
    print("-" * (map_size * 2 + 5))
    print(f"Coin: {player['coin']}")
    print("=" * (map_size * 2 + 5))

def move(direction):
    global player, map_size
    if direction == 'w' and player['y'] > 0:
        player['y'] -= 1
    elif direction == 'a' and player['x'] > 0:
        player['x'] -= 1
    elif direction == 's' and player['y'] < map_size - 1:
        player['y'] += 1
    elif direction == 'd' and player['x'] < map_size - 1:
        player['x'] += 1
    else:
        print("You cannot move that way!")

def main():
    global player
    draw_ui(player['x'], player['y'])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != 'q':
        move(direction)
        
        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        check_event()
        draw_ui(player['x'], player['y'])
        direction = input("Your next move (w/a/s/d/q): ")

if __name__ == '__main__':
    main()