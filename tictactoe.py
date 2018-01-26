import sys

def play():
    width = 3
    height = 3
    grid = generate_grid(width, height)
    print_grid(grid)
    sides = choose_side()
    player_side = sides[0]
    computer_side = sides[1]
    print("Player:", player_side, "Computer:", computer_side)
    while True:
        player_turn(width, height, grid, player_side)
        print_grid(grid)

def generate_grid(width, height):
    field = []
    for row in range(width):
        field.append([])
        for column in range(height):
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

def player_turn(width, height, grid, player_side):
    x, y = get_input(width, height)
    grid[x][y] = ("{}".format(player_side))

def computer_turn(width, height, grid, computer_side):
    """implement minimax algorithm"""
    return None

def get_input(width, height):
    while True:
        try:
            result = input("Give coordinates x,y:\n")
            result = result.split(",")
            result[1] = int(result[1])
            result[0] = int(result[0])
            if result[1] >= width or result[0] >= height or result[1] < 0 or result[0] < 0:
                print("Coordinates are outside of the grid\n")
                continue
        except ValueError:
            print("Give the coordinates as integers\n")
            continue
        except IndexError:
            print("Give two coordinates separated by a comma\n")
            continue
        return result[1], result[0]

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
