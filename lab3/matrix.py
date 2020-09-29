class matrix:
    def __init__(self, matrix_list):
        self.__matrix = matrix_list

    def __repr__(self):
        s = ""
        for row in self.__matrix:
            s += " ".join([str(elem) for elem in row]) + "\n"
        return s

    def __mul__(self, other):
        self_row_len = len(self.__matrix)
        other_row_len = len(other.__matrix)

        # matrix check

        ## matrix cannot be empty
        if self_row_len == 0 or other_row_len == 0:
            raise ValueError("Empty matrix")

        ## every column length has to be the same and cannot be empty
        self_col_len = len(self.__matrix[0])
        for i in range(self_row_len):
            if len(self.__matrix[i]) > 0:
                if len(self.__matrix[i]) == self_col_len:
                    self_col_len = len(self.__matrix[i])
                else:
                    raise ValueError("Invalid Matrix")
            else:
                raise ValueError("Invalid Matrix")

        other_col_len = len(other.__matrix[0])
        for i in range(other_row_len):
            if len(other.__matrix[i]) > 0:
                if len(other.__matrix[i]) == other_col_len:
                    other_col_len = len(other.__matrix[i])
                else:
                    raise ValueError("Invalid Matrix")
            else:
                raise ValueError("Invalid Matrix")

        ## matrix multiplication condition
        if self_col_len != other_row_len:
            raise ValueError("Invalid Matrix for Multiplication")

        # matrix multiplication
        other_transpose = [list(x) for x in zip(*other.__matrix)]
        mul_mat = []
        for self_row in self.__matrix:
            mul_row = []
            for other_col in other_transpose:
                mul_elem = sum([x * y for x, y in zip(self_row, other_col)])
                mul_row.append(mul_elem)
            mul_mat.append(mul_row)

        return matrix(mul_mat)
