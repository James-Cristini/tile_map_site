def get_matrix(tiles):
    # get max range for number of rows and columns"
    max_rows = 0
    max_cols = 0
    for x in tiles:
        if abs(x.horiz_position) > max_rows:
            max_rows = abs(x.horiz_position)
        if abs(x.vert_position) > max_cols:
            max_cols = abs(x.vert_position)

    #  set up a blank matrix based on the number of rows and columns needed
    tile_matrix = [ [[] for x in range(max_rows*2 - 1)] for y in range(max_cols*2 - 1)]

    #  shift the position numbers for each tile over for easier printing
    for x in tiles:
        x.horiz_position += max_rows
        x.vert_position -= max_cols

    #  assign items to each list/tile position - will be the image file names for the large map output
    for y in range(len(tile_matrix)):
        for x in range(len(tile_matrix[y])):
            for i in tiles:
                if i.horiz_position == x and abs(i.vert_position) == y:
                    tile_matrix[y][x] = i

    return tile_matrix
