def play_star_collector_game():
    # Read the size of the field
    n = int(input())

    # Read the field and locate the player
    field = []
    player_position = None

    for i in range(n):
        row = input().split()
        if "P" in row:
            player_position = [i, row.index("P")]
        field.append(row)

    stars_collected = 2
    target_stars = 10
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    while True:
        command = input()
        row, col = player_position
        d_row, d_col = directions[command]
        new_row, new_col = row + d_row, col + d_col

        if 0 <= new_row < n and 0 <= new_col < n:
            if field[new_row][new_col] == "*":
                stars_collected += 1
                field[new_row][new_col] = "."
                player_position = [new_row, new_col]
            elif field[new_row][new_col] == "#":
                stars_collected -= 1
            else:
                player_position = [new_row, new_col]
        else:
            # Teleport to the starting position
            player_position = [0, 0]

        # Mark previous position with a dot
        field[row][col] = "."

        if stars_collected == target_stars:
            print("You won! You have collected 10 stars.")
            break
        elif stars_collected == 0:
            print("Game over! You are out of any stars.")
            break

    # Final position
    final_row, final_col = player_position
    print(f"Your final position is [{final_row}, {final_col}]")

    # Mark the final position on the field
    field[final_row][final_col] = "P"

    # Print the final state of the field
    for row in field:
        print(" ".join(row))


play_star_collector_game()