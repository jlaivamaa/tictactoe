import sys
import random

AREA_WIDTH = 3
AREA_HEIGHT = 3

def play():
    grid = generate_grid()
    print_grid(grid)
    sides = choose_side()
    player_side = sides[0]
    computer_side = sides[1]
    print("Player:", player_side, "Computer:", computer_side)
    get_starting_side()
    while True:
    	player_turn(grid, player_side)
    	computer_turn(grid, computer_side)

def generate_grid():
    field = []
    for row in range(AREA_WIDTH):
        field.append([])
        for column in range(AREA_HEIGHT):
            field[-1].append("#")
    return field

def print_grid(field):
    grid = []
    for row in field:
        grid.append(" ".join(str(tile) for tile in row))
    print("\n".join(grid))

def choose_side():
    letter = ""
    while not(letter == "X" or letter == "O"):
        letter = input("Choose X or O: ").upper();
    
    if letter == "X":
        side = ["X", "O"]
    else:
        side = ["O", "X"]
    return side

def get_starting_side():
	starting_side = random.randint(0, 1)
	print("Computer starts!" if starting_side == 0 else "Player starts!")

def player_turn(grid, player_side):
	print("PLAYER TURN")
	print_grid(grid)
	space_check = False
	while(not space_check):
		x, y = get_input()
		space_check = is_space_free(grid, x, y)
		if(not space_check):
			print("{},{} is full".format(x, y))
	grid[x][y] = ("{}".format(player_side))

def computer_turn(grid, computer_side):
	print("COMPUTER TURN")
	x = random.randint(0,2);
	y = random.randint(0,2);
	grid[x][y] = ("{}".format(computer_side))

def get_input():
    while True:
        try:
            result = input("Give coordinates x,y:\n")
            result = result.split(",")
            result[1] = int(result[1])
            result[0] = int(result[0])
            if result[1] >= AREA_WIDTH or result[0] >= AREA_HEIGHT or result[1] < 0 or result[0] < 0:
                print("Coordinates are outside of the grid\n")
                continue
        except ValueError:
            print("Give the coordinates as integers\n")
            continue
        except IndexError:
            print("Give two coordinates separated by a comma\n")
            continue
        return result[1], result[0]

def is_space_free(grid, x, y):
	return grid[x][y] == "#"

if __name__=="__main__":
    while True:
        try:
            choice = int(input("1 Play\n0 Quit\n"))
            if choice == 1:
                play()
            elif choice == 0:
                sys.exit(0)
            else:
                print("Invalid input")
                continue
        except ValueError:
            print("Input error")
            continue
