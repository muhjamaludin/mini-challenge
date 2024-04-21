def equilateral_right_triangle(side: int):
    """
    Create equilateral right triangle shape using asterik (*) pattern

    Args:
        side (int) : side of triangle
    """

    for i in range(0, side):
        for j in range(0, side):
            if i >= j:
                print("*", end=" ")
        print()
