def rectangular_fill(length: int, width: int):
    """
    Create rectangular shape using asterik (*) pattern

    Args:
        length (int): length of rectangular
        width (int): width of rectangular
    """
    
    for i in range(0, width):
        for j in range(0, length):
            print("*", end=" ")
        print()


def rectangular(length: int, width: int):
    """
    Create rectangular shape with no fill using aserik (*) pattern in every edge

    Args:
        length (int): length of rectangular
        width (int): width of rectangular
    """
    
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
