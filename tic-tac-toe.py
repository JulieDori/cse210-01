'''
Tic-Tac-Toe Game
By: Julie Ann Doricarion
'''


def main():
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    winning_combi = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                     (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    def draw_board():
        print(f"{grid[0]}|{grid[1]}|{grid[2]}")
        print("_+_+_")
        print(f"{grid[3]}|{grid[4]}|{grid[5]}")
        print("_+_+_")
        print(f"{grid[6]}|{grid[7]}|{grid[8]}")

    def player_1():
        num = choose_num()
        if grid[num] == "X" or grid[num] == "O":
            print("Already occupied! Try again.")
            player_1()
        else:
            grid[num] = "X"

    def player_2():
        num = choose_num()
        if grid[num] == "X" or grid[num] == "O":
            print("Already occupied! Try again.")
            player_2()
        else:
            grid[num] = "O"

    def choose_num():
        while True:
            a = int(input())
            a -= 1
            if a in range(0, 9):
                return a

    def check():
        count = 0
        # for a in winning_combi:
        if grid[0] == grid[1] == grid[2] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[3] == grid[4] == grid[5] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[6] == grid[7] == grid[8] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[0] == grid[3] == grid[6] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[1] == grid[4] == grid[7] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[2] == grid[5] == grid[8] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[0] == grid[4] == grid[8] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True
        elif grid[2] == grid[4] == grid[6] == "X":
            print("Player 1 wins")
            print("Congratulations!")
            return True

        elif grid[0] == grid[1] == grid[2] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[3] == grid[4] == grid[5] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[6] == grid[7] == grid[8] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[0] == grid[3] == grid[6] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[1] == grid[4] == grid[7] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[2] == grid[5] == grid[8] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[0] == grid[4] == grid[8] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        elif grid[2] == grid[4] == grid[6] == "O":
            print("Player 2 wins")
            print("Congratulations!")
            return True
        for a in range(9):
            if grid[a] == "X" or grid[a] == "O":
                count += 1
            if count == 9:
                print("Draw!")
                print("The game ends!")
                return True

    while not end:
        draw_board()
        end = check()
        if end == True:
            break
        print(f"x's turn to choose a square (1-9): ")
        player_1()
        draw_board()
        end = check()
        if end == True:
            break
        print(f"o's turn to choose a square (1-9): ")
        player_2()


if __name__ == "__main__":
    main()
