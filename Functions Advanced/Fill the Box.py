def fill_the_box(height, length, width, *cubes):
    total_volume = height * length * width

    cubes_volume = 0
    for cube in cubes:
        if cube == "Finish":
            break

        cubes_volume += cube

    if cubes_volume > total_volume:
        return f"No more free space! You have {cubes_volume - total_volume} more cubes."
    else:
        return f"There is free space in the box. You could put {total_volume - cubes_volume} more cubes."
