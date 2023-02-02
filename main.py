field = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
active_player = "X"
run = True


def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])


def next_move():
    while True:

        player_move = input("Bitte gib ein Feld an: ")

        player_move = int(player_move)

        if player_move >= 1 and player_move <= 9:
            if field[player_move] == "X" or field[player_move] == "O":
                print("Spielfeld ist belegt")
            else:
                return player_move
        else:
            print("Die Zahl muss zwischen 1 u. 9 liegen!")


def check_win():
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]

    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]

    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]


def check_draw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[
            4] != "4" and field[5] != "5" and field[6] != "6" and field[
                7] != "7" and field[8] != "8" and field[9] != "9":
        return True

while run:
    print_field()
    player_move = next_move()
    field[player_move] = active_player
    winner = check_win()

    if winner:
        print("Spieler " + winner + " hat gewonnen")
        run = False

    if check_draw():
        print("Spiel ist unentschieden ausgegangen")
        run = False

    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"

    print("")