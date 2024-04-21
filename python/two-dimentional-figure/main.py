from src import rectangular, square, triangle

def print_rectangular():
    length, width = 7, 5
    print("Rectangular {} x {}".format(length, width))
    print()
    rectangular.rectangular_fill(length, width)
    print()
    rectangular.rectangular(length, width)
    print()
    
def print_square():
    side = 6
    print("Square {}".format(side))
    print()
    square.square_fill(side)
    print()
    square.square(side)
    print()
    
def print_triangle():
    base = 8
    print("Equilateral right triangle base {}".format(base))
    print()
    triangle.equilateral_right_triangle(side=base)
    print()

print("-------------------------------")
print_rectangular()
print("-------------------------------")
print_square()
print("-------------------------------")
print_triangle()
