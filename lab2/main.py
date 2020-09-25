from matrix import matrix
from figure import triangle
from figure import rectangle
from figure import circle


def prob_1():
    input_file = open("matrix.txt", "r")

    lines = input_file.readlines()

    input_file.close()

    mat_1 = matrix(eval(lines[0]))
    mat_2 = matrix(eval(lines[1]))

    print("MATRIX 1")
    print(mat_1)

    print("MATRIX 2")
    print(mat_2)

    print("MATRIX 1 * MATRIX 2")
    print(mat_1 * mat_2)


def prob_2():
    t = triangle("red", 3, 4)
    print(t)
    r = rectangle("blue", 5, 5)
    print(r)
    c = circle("green", 2)
    print(c)


if __name__ == "__main__":
    prob_1()
    prob_2()
