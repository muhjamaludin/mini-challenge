def right_triangle(base: int, height: int):
    """
    Create right triangle shape using asterik (*) pattern

    Args:
        base (int) : base of triangle
        height (int) : height of triangle
    """
    print()

    for i in range(0, height):
        for j in range(0, base):
            if i >= j:
                print("*", end=" ")
        print()

    print()


right_triangle(7, 5)
