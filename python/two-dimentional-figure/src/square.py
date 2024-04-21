def square_fill(n: int):
    """
    Create square shape using asterik (*) pattern

    Parameters:
    n (int): Size of square
    """
    
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
        print()


def square(n: int):
    """
    Create square with no fill using asterik (*) in every edge

    Parameters:
    n (int): Size of square
    """
    
    for i in range(0, n):
        for j in range(0, n):
            if i == 0 or i == (n - 1):
                print("*", end=" ")
            else:
                if j == 0 or j == (n - 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()
