def rectangular_fill(length: int, width: int):
    """
    Create rectangular shape using asterik (*) pattern

    Args:
        length (int): length of rectangular
        width (int): width of rectangular
    """
    print()

    for i in range(0, width):
        for j in range(0, length):
            print("*", end=" ")
        print()

    print()


def rectangular(length: int, width: int):
    """
    Create rectangular shape with no fill using aserik (*) pattern in every edge

    Args:
        length (int): length of rectangular
        width (int): width of rectangular
    """
    print()

    for i in range(0, width):
        for j in range(0, length):
            if i == 0 or i == (width - 1):
                print("*", end=" ")
            else:
                if j == 0 or j == (length - 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

    print()


rectangular_fill(8, 5)
rectangular(8, 5)
