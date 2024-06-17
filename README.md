The SparseMatrix class represents a sparse matrix, which is a matrix primarily composed of zero-valued elements. This class provides methods to initialize the matrix, load data from a file, set and get elements, and perform addition and subtraction with another sparse matrix.

1.`init `Method
Initializes the matrix either from a file or by specifying the number of rows and columns.
Uses read_from_file to read the matrix from a file.
2. `read_from` file Method
Reads the sparse matrix from a file.
Parses the number of rows and columns.
Extracts the matrix elements and stores them in a dictionary.
3. `get` element Method
Returns the value at the specified row and column.
Returns 0 if the element is not explicitly stored (as it's a sparse matrix).
4. `set `element Method
Sets the value at the specified row and column.
Removes the element if the value is set to 0 to maintain the sparsity.
5.`str` Method
Provides a string representation of the sparse matrix for easy printing.
