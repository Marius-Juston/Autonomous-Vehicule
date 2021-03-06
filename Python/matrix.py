import numbers


def zeroes(height: int, width: int):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)


def identity(n: int):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


def dot_product(vector_a: iter, vector_b: iter) -> float:
    return sum(a * b for a, b in zip(vector_a, vector_b))


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.")

        if self.h == 2:
            a, b, c, d = *self[0], *self[1]
            det = a * d - b * c

            return det

        return self[0][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a non-square matrix.")

        return sum(self[r][r] for r in range(self.h))

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        det = self.determinant()

        if det == 0:
            raise (ValueError, "Cannot determine the inverse if determinant is 0")

        if self.h == 2:
            return 1 / det * (self.trace() * identity(self.h) - self)

        return Matrix([[1 / self[0][0]]])

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        return Matrix([[self[r][c] for r in range(self.h)] for c in range(self.w)])

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx: int):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")
            #
        return Matrix([[a + b for a, b in zip(ra, rb)] for ra, rb in zip(self, other)])

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        return -1 * self

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")
            #
        return Matrix([[a - b for a, b in zip(ra, rb)] for ra, rb in zip(self, other)])

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        other = other.T()
        return Matrix([[dot_product(self[r], other[c]) for c in range(other.h)] for r in range(self.h)])

    def __rmul__(self, other: float):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            return Matrix([[other * e for e in r] for r in self])
