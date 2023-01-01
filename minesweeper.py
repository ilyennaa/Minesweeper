WIDTH = 300
HEIGHT = 300



def draw():
    square_side = 32
    red = (255, 0, 0)
    left_pos = 5
    top_pos = 5
    screen.fill((0, 0, 0))

    # Populate window with a 9x9 grid of tiles
    for i in range(0, 9):
        for j in range(0, 9):
            tile = Rect((left_pos, top_pos), (square_side, square_side))
            screen.draw.rect(tile, red)
            left_pos += square_side

        left_pos = 5
        top_pos += square_side
