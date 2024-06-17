ass SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        if matrix_file_path:
            self.num_rows, self.num_cols, self.elements = self.read_from_file(matrix_file_path)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.elements = {}
        else:
            raise ValueError("Either matrix_file_path or num_rows and num_cols must be provided")

    def read_from_file(self, matrix_file_path):
        with open(matrix_file_path, 'r') as file:
            lines = file.readlines()
        
        num_rows = int(lines[0].split('=')[1])
        num_cols = int(lines[1].split('=')[1])
        elements = {}
        
        for line in lines[2:]:
            line = line.strip()
            if line.startswith('(') and line.endswith(')'):
                row, col, value = map(int, line[1:-1].split(','))
                if row not in elements:
                    elements[row] = {}
                elements[row][col] = value
        
        return num_rows, num_cols, elements

    def get_element(self, curr_row, curr_col):
        if curr_row in self.elements and curr_col in self.elements[curr_row]:
            return self.elements[curr_row][curr_col]
        return 0

    def set_element(self, curr_row, curr_col, value):
        if value != 0:
            if curr_row not in self.elements:
                self.elements[curr_row] = {}
            self.elements[curr_row][curr_col] = value
        else:
            if curr_row in self.elements and curr_col in self.elements[curr_row]:
                del self.elements[curr_row][curr_col]
                if not self.elements[curr_row]:
                    del self.elements[curr_row]

    def __str__(self):
        matrix_str = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for row in self.elements:
            for col in self.elements[row]:
                value = self.elements[row][col]
                matrix_str += f"({row}, {col}, {value})\n"
        return matrix_str

if __name__ == "__main__":
    sparse_matrix = SparseMatrix(matrix_file_path='sparse_matrix.txt')
    print(sparse_matrix)
    print(sparse_matrix.get_element(0, 381))  
    sparse_matrix.set_element(1, 1, 999)
    print(sparse_matrix.get_element(1, 1))  
    print(sparse_matrix)
